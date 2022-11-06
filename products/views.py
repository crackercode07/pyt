from django.http import HttpResponse
from django.shortcuts import render
from .models import product

def products(request):
    products = product.objects.all()
    return render(request, 'products.html', {'products' : products})


def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')