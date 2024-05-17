from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    selected_category = None
    if request.method == 'POST':
        selected_category = request.POST.get('selectedcategory')
        if selected_category and selected_category != 'None':
            pro = Product.objects.filter(category=selected_category)
        else:
            pro = Product.objects.all()
    else:
        pro = Product.objects.all()
    
    context = {'pro': pro, 'selected_category': selected_category}
    return render(request, 'products/products.html', context)



def product(request, name):
    product = get_object_or_404(Product, name=name)
    return render(request, 'products/product.html', {'product': product})



