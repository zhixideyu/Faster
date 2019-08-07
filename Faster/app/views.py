from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
# Create your views here.


def index(request):
    return render(request, 'index.html')


def details(request):
    return render(request, 'content.html')

