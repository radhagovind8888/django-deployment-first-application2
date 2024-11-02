from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.

#single application with multiple views...

def f1(request):
        return HttpResponse("<h2>Good Morning All....</h2><hr/>");

def f2(request):
        return HttpResponse("<h3>How are you...</h3><hr/>");
        
def f3(request):
        return HttpResponse("<h4>Whats going.....</h4><hr/>")