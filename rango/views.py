from django.shortcuts import render

from django.http import HttpResponse

def index(request): # create index view
    return HttpResponse("Rango says hey there partner!") # return HttpResponse object
