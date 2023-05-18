from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    S="<h1> Hellow Student welcome to Mahesh Sir Django Classes<h1>"
    return HttpResponse(S)

