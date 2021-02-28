from django.shortcuts import render
import json
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


def products(request, pk=None):
    """
    Function products corresponds to products.html and allows to view it
    :param request:
    :return: render with request and template for web page specified
    """
    context = {
        "title": "GeekShop - Каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    }

    return render(request, "mainapp/products.html", context)
