from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f22(request): 
	return HttpResponse("<h1>Hello, Good Morning User..!! what special today...</h1><hr/>");
