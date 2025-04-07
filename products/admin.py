from django.contrib import admin
from .models.product import Product
from .models.specification import ProductSpecification

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductSpecification)