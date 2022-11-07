from django.shortcuts import render, HttpResponseRedirect

from .models import Product, ProductCategory, Basket


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


def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
