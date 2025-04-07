from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, 
            null=True, blank=True, related_name='subcategories' )

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_full_path(self):
        parts = [self.name]
        parent = self.parent
        while parent:
            parts.append(parent.name)
            parent = parent.parent
        return " > ".join(reversed(parts))


class SpecificationTemplate(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='spec_templates')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.category.name})"