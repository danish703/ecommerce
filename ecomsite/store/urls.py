from django.urls import path
from .views import store,product_details,search
urlpatterns = [
    path('',store,name='store'),
    path('<slug:category_slug>',store,name="productByCategory"),
    path('<slug:category_slug>/<slug:product_slug>', product_details, name="product_details"),
    path('search/',search,name='search'),
]