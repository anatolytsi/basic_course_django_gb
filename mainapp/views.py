from django.shortcuts import render

# Create your views here.
# USER: functions = views = controllers


def index(request):
    """
    Function index corresponds to index.html and allows to view it
    :param request:
    :return: render with request and template for web page specified
    """
    return render(request, 'mainapp/index.html')


def products(request):
    """
    Function products corresponds to products.html and allows to view it
    :param request:
    :return: render with request and template for web page specified
    """
    return render(request, 'mainapp/products.html')
