from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse

# Create your views here.
from trades.models import Category, Product


def index(request):
    return render(request, 'trades/index.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'trades/products.html', {'categories' : categories})

def by_category(request, category_id, page):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    per_page = 1
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)

    context = {'products' : products_paginator, 'category': category}
    return render(request, 'trades/products_to_buy.html', context)


