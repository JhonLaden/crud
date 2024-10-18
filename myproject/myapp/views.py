from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    return HttpResponse('hello world')

def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'myapp/index.html')

def product_details(request, id):
    products = Product.objects.get(id=id)
    context = {
        'products': products,
    }

    return render(request, 'myapp/viewproduct.html')


def add_product(request): 
    if request.method=='POST':
        name = request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        product = Product(name=name, price=price, description=description)
        product.save()
    return render(request, 'myapp/addproduct.html')