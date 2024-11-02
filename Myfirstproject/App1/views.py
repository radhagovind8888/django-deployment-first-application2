from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Single Project  with multiple applications....

def f11(request): 
	return HttpResponse("<h2>Hello, Good Morning User..!! Have a Nice day...</h2><hr/>");
