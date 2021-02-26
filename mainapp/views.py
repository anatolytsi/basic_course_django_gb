from django.shortcuts import render
import json
from mainapp.models import  Product, ProductCategory

# Create your views here.
# USER: functions = views = controllers


def index(request):
    """
    Function index corresponds to index.html and allows to view it
    :param request:
    :return: render with request and template for web page specified
    """
    context = {
        "title": "GeekShop"
    }

    return render(request, "mainapp/index.html", context)


def products(request):
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
