from django.shortcuts import render
from django.http import HttpResponse

from models import Drink

def index(request):
	context = {}
	drinks = Drink.objects.all()
	context['rows'] = [drinks[i:i + 3] for i in xrange(0, 9, 3)]

	num_pages = (len(drinks)-1)/9 + 1
	context['pagination'] = range(1, num_pages+1)
	context['active_page'] = 1
	context['max_page'] = num_pages

	return render(request, 'app/index.html', context)
