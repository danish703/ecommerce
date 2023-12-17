from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Product
from Category.models import Category
from Cart.models import CartItem,Cart
from Cart.views import  _cartId
from django.db.models import Q
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def store(request,category_slug=None):
    products= None
    category = None
    if category_slug != None:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category,is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products':paged_products,
        'product_count':product_count
    }
    return render(request,'store.html',context)


def product_details(request,category_slug,product_slug):
    product = get_object_or_404(Product,slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cartId=_cartId(request),product=product).exists()
    context = {
        'product':product,
        'incart':in_cart
    }
    return render(request,'product_details.html',context)

def search(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        if q:
            result = Product.objects.order_by('-created_at').filter(Q(description__icontains=q)|Q(product_name__icontains=q))
        context={
            'products':result,
            'product_count':result.count(),
        }
    else:
        context = {'products':None}
    return render(request,'store.html',context)