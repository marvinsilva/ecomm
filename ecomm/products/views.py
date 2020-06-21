from django.shortcuts import render, redirect

from ecomm.products.forms import ProductModelForm
from ecomm.products.models import Product


def list_products(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/list.html', context=context)


def create_product(request):
    if request.method == 'POST':
        # Salvar form
        form = ProductModelForm(request.POST)
        if form.is_valid():
            # True -> é valido
            form.save()
            return redirect('products:list')
    else:
        # Get form
        form = ProductModelForm()

    context = {
        'form': form
    }
    return render(request, 'products/create.html', context=context)
