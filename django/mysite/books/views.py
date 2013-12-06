from django.shortcuts import render
from django.http import HttpResponse
from books.models import Books

# Create your views here.
def search_form(request):
	return render(request,'search_form.html')

def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			books = Books.objects.filter(title__icontains=q)
			return render(request,'search_result.html',{'books':books, 'query':'q'})	
	return render(request,'search_form.html',{'error':error})