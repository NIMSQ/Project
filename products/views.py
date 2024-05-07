from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    pro = Product.objects.all()
    x = {'pro':pro}
    return render(request, 'products/products.html', x)


def product(request, name):
    product = get_object_or_404(Product, name=name)
    return render(request, 'products/product.html', {'product': product})
