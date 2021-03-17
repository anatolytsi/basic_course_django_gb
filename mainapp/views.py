from django.shortcuts import render
from django.core.paginator import Paginator

from mainapp.models import Product, ProductCategory

# Create your views here.
# USER: functions = views = controllers


def index(request):
    """
    Function index corresponds to index.html and allows to view it
    :param request:
    :return: render with request and template for web page specified
    """
    context = {
        "title": "GeekShop",
        "header": "GeekShop Store",
        "description": "Новые образы и лучшие бренды на GeekShop Store.Бесплатная доставка по всему миру! Аутлет: до "
                       "-70% Собственный бренд. -20% новым покупателям. "
    }

    return render(request, "mainapp/index.html", context)


def products(request, category_id=None, page=1):
    """
    Function products corresponds to products.html and allows to view it
    :param request:
    :param page:
    :param category_id:
    :return: render with request and template for web page specified
    """
    context = {
        "title": "GeekShop - Каталог",
        "categories": ProductCategory.objects.all()
    }

    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by("-price")
    else:
        products = Product.objects.all().order_by("-price")
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page)
    context.update({"products": products_paginator})
    return render(request, "mainapp/products.html", context)

