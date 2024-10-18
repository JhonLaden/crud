from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, get_object_or_404
# Create your views here.

def index(request):
    return HttpResponse('hello world')

def products(request):
    products = Product.objects.all()  # Fetch all products from the database
    context = {
        'products': products,  # Pass products to the template
    }
    return render(request, 'myapp/index.html', context)  # Pass context to render


def product_details(request, id):
    # Get the single product or return 404 if not found
    product = get_object_or_404(Product, id=id)
    
    context = {
        'product': product,  # Use 'product' in singular since it's a single object
    }
    
    return render(request, 'myapp/details.html', context)

def add_product(request): 
    if request.method=='POST':
        name = request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        product = Product(name=name, price=price, description=description)
        product.save()
    return render(request, 'myapp/addproduct.html')


def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price
        request.POST.get('price')
        product.description = request.POST.get('description')
        product.save()
        return redirect('/myapp/products')
    context = {
        'product': product,
    }
    return render(request, 'myapp/updateproduct.html', context)


def delete_product(request, id): 
    product = Product.objects.get(id=id) 
    context = {
        'product': product,
    }
    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/products')
    return render(request, 'myapp/deleteproduct.html', context)
