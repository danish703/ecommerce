from django.db import models
from django.urls import reverse
from Category.models import Category
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    stock = models.IntegerField()
    images = models.ImageField(upload_to='images/products')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse("product_details",args=[self.category.slug,self.slug])