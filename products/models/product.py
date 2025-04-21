from django.db import models
from django.contrib.auth import get_user_model
from categories.models import Category

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(
        max_length=20, choices=[("new", "New"), ("used", "Used")], default="used"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title