from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def function1(request):
    return HttpResponse('Function N1')

def function2(request):
    return HttpResponse('Function N2')    

def function3(request):
    return HttpResponse('Function N3')