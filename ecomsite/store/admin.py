from django.contrib import admin
from .models import Product,ProductVariation
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name","price","stock","created_at","is_available",)
    prepopulated_fields = {"slug":("product_name",)}

admin.site.register(Product,ProductAdmin)


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ('product','variationChoice','variationValue','is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active','product','variationChoice')

admin.site.register(ProductVariation,ProductVariationAdmin)