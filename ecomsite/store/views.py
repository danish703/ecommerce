from django.shortcuts import render,get_object_or_404
from .models import Product
from Category.models import Category
# Create your views here.
def store(request,category_slug=None):
    products= None
    category = None
    if category_slug != None:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category,is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products':products,
        'product_count':product_count
    }
    return render(request,'store.html',context)


def product_details(request,category_slug,product_slug):
    product = get_object_or_404(Product,slug=product_slug)
    context = {
        'product':product
    }
    return render(request,'product_details.html',context)