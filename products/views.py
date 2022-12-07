from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import ProductForm
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html',
                  {'products': products})


def new_product(request):
    if request.method == 'GET':
        context_form = {'form': ProductForm()}
        return  render(request, 'products/product_form.html', context_form)
    else:
        try:
            form = ProductForm(request.POST)
            form.save()
            return redirect('products:index')
        except ValueError:
            context = {'form': ProductForm(), 'error': 'Bad data, try again'}
            return render(request, 'products/product_form.html', context)


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'products/product_details.html', context)
