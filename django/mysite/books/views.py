# -*- coding: utf-8 -*-
from django.shortcuts import render
#from django.http import HttpResponseRedirect
from books.models import Books
from django.core.mail import send_mail

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

def contact(request):
	errors=[]
	if request.method =="POST":
		if not request.POST.get('subject',''):
			errors.append('Введите тему сообщения')
		if not request.POST.get('message',''):
			errors.append('Введите сообщение')
		if request.POST.get('email','') and '@' not in request.POST['email']:
			errors.append("Не валидный емайл")
		if not errors:
			mes = 'mes'
			# send_mail(
			# 	request.POST['subject'],
			# 	request.POST['message'],
			# 	request.POST.get('email','noreplay@yourmail.ru'),
			# 	['siteowner@example.com'],
			# 	)
			return render(request,'contact_form.html',{'mes':mes})#HttpResponseRedirect('/contact/thanks/')
	return render(request,'contact_form.html',{'errors':errors})		
