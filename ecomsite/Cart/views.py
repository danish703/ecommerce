from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from store.models import Product,ProductVariation
from .models import Cart,CartItem
# Create your views here.
def _cartId(request):
    cart  = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def subtractQuantity(request,cart_item_id):
    cart = Cart.objects.get(cartId=_cartId(request))
    cartItem = CartItem.objects.get(id=cart_item_id,cart=cart)
    if cartItem.quantity>1:
        cartItem.quantity-=1
        cartItem.save()
    else:
        cartItem.delete()
    return redirect('cart')

def removeFromCart(request,cart_item_id):
    cart = Cart.objects.get(cartId=_cartId(request))
    cartItem = CartItem.objects.get(id=cart_item_id,cart=cart)
    cartItem.delete()
    return redirect('cart')


def cart(request,quantity=0,total=0,cartItems=None):
    try:
        cart = Cart.objects.get(cartId = _cartId(request))
        cartItems = CartItem.objects.filter(cart=cart,is_active=True)
        for cartitem in cartItems:
            total += cartitem.product.price*cartitem.quantity
            quantity += quantity+cartitem.quantity
        tax = (2*total)/100
        grand_total = total+tax
    except Exception as e:
        print(e)
    context = {
        'total':total,
        'cartItems':cartItems,
        'quantity':quantity,
        'tax':tax,
        'grand_total':grand_total,
    }
    return render(request,'cart.html',context)



def addToCart(request,product_id):
    product = Product.objects.get(id=product_id)
    product_variation = []
    for key in request.POST:
        value = request.POST[key]
        try:
            variation = ProductVariation.objects.get(product=product,variationChoice__iexact=key,variationValue__iexact=value)
            product_variation.append(variation)
        except:
            pass
    try:
        cart = Cart.objects.get(cartId=_cartId(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cartId=_cartId(request))

    currentProducts = CartItem.objects.filter(product=product,cart=cart)
    exiting_products_variation = []
    ids = []
    if len(currentProducts)>0:
        for i in currentProducts:
            exiting_products_variation.append(list(i.variation.all()))
            ids.append(i.id)

        if product_variation in exiting_products_variation:
            index = exiting_products_variation.index(product_variation)
            id = ids[index]
            cart_item = CartItem.objects.get(product=product,id=id)
            cart_item.quantity +=1
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(product=product,cart=cart,qunatity=1)
            if len(product_variation)>0:
                cart_item.variation.clear()
                for i in product_variation:
                    cart_item.variation.add(i)
            cart_item.save()
    else:
        cart_item = CartItem.objects.create(product=product,cart=cart,quantity=1)
        if len(product_variation)>0:
           cart_item.variation.clear()
           for i in product_variation:
               cart_item.variation.add(i)
        cart_item.save()
    return redirect('cart')

def increaseQuantity(request,cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity+=1
        cart_item.save()
    except:
        pass
    return redirect('cart')