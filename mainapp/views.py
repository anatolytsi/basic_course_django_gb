from django.shortcuts import render
import json

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
        "title": "GeekShop - Каталог"
    }

    # Get JSON array
    with open("mainapp/fixtures/products.json", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Add products to context
    context.update({"products": data})

    return render(request, "mainapp/products.html", context)
