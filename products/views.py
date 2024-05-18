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



from django.shortcuts import render, redirect
from .models import Product


def addProduct(request):
    if request.method == 'POST':
        nameval = request.POST.get('name')
        contentval = request.POST.get('content')
        priceval = request.POST.get('price')
        imageval = request.FILES.get('image')
        activeval = request.POST.get('active') == 'on'
        categoryval = request.POST.get('category')
        
        
        
            
        new_product = Product(name=nameval,content=contentval, price=priceval, image=imageval,active=activeval,category=categoryval)
            
        new_product.save()
            
            
        return redirect('products')
    
    return render(request, 'products/addProduct.html')


def updateProduct(request, pid):
    obj = get_object_or_404(Product, id=pid)
    
    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.content = request.POST.get('content')
        obj.price = request.POST.get('price')
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
        obj.active = 'active' in request.POST
        obj.category = request.POST.get('category')
        
        obj.save()
        return redirect('products')  
    
    context = {'obj': obj}
    return render(request, 'products/updateProduct.html', context)
