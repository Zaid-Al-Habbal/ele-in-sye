from django.contrib import admin
from categories.models import Category, SpecificationTemplate

# Register your models here.
admin.site.register(Category)
admin.site.register(SpecificationTemplate)