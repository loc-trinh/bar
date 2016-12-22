from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q

from models import Drink

def index(request):
	context = {}
	
	drinks = Drink.objects.all()
	num_pages = (len(drinks)-1)/9 + 1
	context['pagination'] = range(1, num_pages+1)
	context['active_page'] = 1
	context['max_page'] = num_pages

	drinks = drinks[0:9]
	context['rows'] = [drinks[i:i + 3] for i in xrange(0, 9, 3)]
	
	return render(request, 'app/index.html', context)

def page(request, page_id):
	page_id = int(page_id)

	if page_id == 1:
		return redirect("/")

	context = {}
	
	drinks = Drink.objects.all()
	num_pages = (len(drinks)-1)/9 + 1
	context['pagination'] = range(1, num_pages+1)
	context['active_page'] = page_id
	context['max_page'] = num_pages

	drinks = drinks[(page_id-1)*9:page_id*9]
	context['rows'] = [drinks[i:i + 3] for i in xrange(0, 9, 3)]
	
	return render(request, 'app/index.html', context)

def favorite(request):
	return render(request, 'app/favorite.html', {})

def available(request):
	return render(request, 'app/available.html', {})

def special(request):
	return render(request, 'app/thespecial.html', {})

def search(request):
	query = request.GET["query"]
	context = {}
	drinks = Drink.objects.filter(reduce(lambda x, y: x & y, [Q(name__icontains=word) | Q(ingridients__icontains=word) | Q(instructions__icontains=word) for word in query.split(",")]))
	context['rows'] = [drinks[i:i + 3] for i in xrange(0, len(drinks), 3)]
	return render(request, 'app/search.html', context)
