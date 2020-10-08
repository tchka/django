from django.contrib import admin
from mainapp.models import Product
from mainapp.models import ProductCategory
from mainapp.models import Gallery


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Gallery)