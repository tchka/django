from django.contrib import admin
from mainapp.models import Product
from mainapp.models import ProductCategory

admin.site.register(Product)
admin.site.register(ProductCategory)