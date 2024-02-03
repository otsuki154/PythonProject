from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'pages/index.html',{})

def category(request):
    return render(request, 'pages/category.html',{})

def artical(request):
    return render(request, 'pages/artical.html',{})

def feed(request):
    return render(request, 'pages/feed.html',{})

def search(request):
    return render(request, 'pages/search.html',{})
