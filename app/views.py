from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.db.models import Q

from models import Drink

def index(request):
	drinks = Drink.objects.order_by("name")
	num_pages = (len(drinks)-1)/9 + 1

	context = {}
	context['max_page'] = num_pages
	context['active_page'] = 1
	context['pagination'] = range(1, num_pages+1)
	context['rows'] = [drinks[i:i + 3] for i in xrange(0, 9, 3)]
	
	return render(request, 'app/index.html', context)

def page(request, page_id):
	page_id = int(page_id)

	if page_id == 1:
		return redirect("/")

	drinks = Drink.objects.order_by("name")
	num_pages = (len(drinks)-1)/9 + 1

	context = {}
	context['max_page'] = num_pages
	context['active_page'] = page_id
	context['pagination'] = range(1, num_pages+1)
	
	drinks = drinks[(page_id-1)*9:page_id*9]
	context['rows'] = [drinks[i:i + 3] for i in xrange(0, 9, 3)]
	
	if page_id <= num_pages:
		return render(request, 'app/index.html', context)
	else:
		raise Http404()

def search(request):
	query = request.GET["query"]
	query_list = query.split(",")
	drinks = Drink.objects.filter(reduce(lambda x, y: x & y, [Q(name__icontains=word) | Q(ingridients__icontains=word) | Q(instructions__icontains=word) for word in query_list]))
	
	context = {}
	context['query'] = query
	context['found'] = True if len(drinks) > 0 else False
	context['rows'] = [drinks[i:i + 3] for i in xrange(0, len(drinks), 3)]
	
	return render(request, 'app/search.html', context)

def favorite(request):
	return render(request, 'app/favorite.html', {})

def available(request):
	drinks = Drink.objects.filter(available = True).order_by("name")

	context = {'drinks':drinks}
	return render(request, 'app/available.html', context)
	

def special(request):
	return render(request, 'app/thespecial.html', {})


