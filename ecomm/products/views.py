from django.shortcuts import render, redirect, get_object_or_404

from ecomm.products.forms import ProductModelForm
from ecomm.products.models import Product


def list_products(request):
    products = Product.objects.all()

    context = {
        'products': products,
        'products_empty': []
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


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product.delete()
        return redirect('products:list')
    context = {
        "product": product
    }
    return render(request, "products/delete.html", context)


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        # salvar form
        form = ProductModelForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        # GET
        form = ProductModelForm(instance=product)

    context = {
        'form': form,
    }

    return render(request, 'products/update.html', context=context)
