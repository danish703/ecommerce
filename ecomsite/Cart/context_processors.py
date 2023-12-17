from .views import _cartId
from .models import Cart,CartItem

def counter(request):
    count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cartId=_cartId(request))
            cartItems = CartItem.objects.filter(cart=cart[:1])
            for item in cartItems:
                count += item.quantity
        except:
            pass
    return dict(cartCount=count)