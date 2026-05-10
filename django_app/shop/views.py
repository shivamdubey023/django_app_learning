from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop(request):
    return HttpResponse("This is shopping page")

def payment(request):
    return HttpResponse("This is payment page")