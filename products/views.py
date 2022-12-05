from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('New Products')


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'products/product_details.html', context)
