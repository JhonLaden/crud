from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('products/', views.products, name = 'products'),
    path('productdetails/', views.product_details, name = 'product_products'),

    path('', views.index, name = 'myapp'),
    
]