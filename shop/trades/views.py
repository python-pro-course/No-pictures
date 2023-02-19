from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

# Create your views here.
from trades.models import Category, Product, Basket


def index(request):
    return render(request, 'trades/index.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'trades/products.html', {'categories': categories})

def by_category(request, category_id, page):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    per_page = 1
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)

    context = {'products': products, 'paginator' : products_paginator, 'category': category}
    return render(request, 'trades/products_to_buy.html', context)
def basket1(request):
    return render(request, 'trades/basket.html')



def basket(request, product_id):
    product = Product.objects.filter(id=product_id)
    user_baskets = Basket.objects.filter(user=request.user)
    if not user_baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = user_baskets.last()
        basket.quantity += 1
        basket.save()


    return HttpResponseRedirect(request.META['HTTP_REFERER'])


