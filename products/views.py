from django.shortcuts import render

from .models import Product, ProductCategory


def index(request):
    return render(request, 'products/index.html', {
        'title': 'Store'
    })


def products(request):
    return render(request, 'products/products.html', {
        'title': 'Store - products',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    })
