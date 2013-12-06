# -*- coding: utf-8 -*-
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello World выавы")

def my_homepage_view(request):
	return HttpResponse('it is your first page')