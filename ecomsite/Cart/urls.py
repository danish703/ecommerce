from django.urls import path
from .views import cart,addToCart,subtractQuantity,removeFromCart,increaseQuantity
urlpatterns = [
    path('',cart,name='cart'),
    path('addtocart/<int:product_id>',addToCart,name="addToCart"),
    path('subtractfromcart/<int:product_id>',subtractQuantity,name="subtractfromcart"),
    path('increasequantity/<int:cart_item_id>',increaseQuantity,name="increasequantity"),
    path('remove/<int:cart_item_id>',removeFromCart,name="removeFromCart"),
]