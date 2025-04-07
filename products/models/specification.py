from django.db import models
from categories.models import SpecificationTemplate
from .product import Product  

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    template = models.ForeignKey(SpecificationTemplate, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.template.name}: {self.value}"
