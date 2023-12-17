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

variationChoices = (
    ('Color','color'),
    ('Size','size')
)

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variationChoice='Color',is_active=True)
    def sizes(self):
        return super(VariationManager,self).filter(variationChoice='Size',is_active=True)
class ProductVariation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variationChoice = models.CharField(max_length=30,choices=variationChoices)
    variationValue = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    objects = VariationManager()
    class Meta:
        unique_together = ('product','variationChoice','variationValue')

    def __str__(self):
        return self.variationValue