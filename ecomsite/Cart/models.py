from django.db import models
from store.models import Product,ProductVariation
# Create your models here.
class Cart(models.Model):
    cartId = models.CharField(max_length=200,blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cartId

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation = models.ManyToManyField(ProductVariation,blank=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return  self.quantity*self.product.price
    def __unicode__(self):
        return self.product