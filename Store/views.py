from django.shortcuts import render
from .models import Product, Quality_shelf

def index(request):
    if request.method == 'GET':
        product_data = Product.objects.all()
        shelf = Quality_shelf.objects.all()
        return render(request, 'index.html', {
            'product_data' : product_data,
            'quality_shelf': shelf, 
        })
    
def checkout(request, pk):
    product_data = Product.objects.get(id = pk)
    shelf = Quality_shelf.objects.get(id = pk)

    if product_data is not None:

        return render (request, 'checkout.html', {
            'product_data' : product_data,
            
        })
    
    elif shelf is not None:
        return render (request, 'checkout.html', {
            'shelf': shelf,
        })

def product_list(request, product_name):
    product = Product.objects.filter(product_category = product_name)

    if product is not None:
        context = {
            'details': product,
        }
        return render (request, 'products.html', context)