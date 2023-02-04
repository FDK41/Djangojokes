from django.shortcuts import render
from django.http import HttpResponse

def jokes(request):
    return HttpResponse("Hello world!")