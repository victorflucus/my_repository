# product.models.py
from django.db import models

class Product(models.Model):
    name = models.TextField()
    featured = models.BooleanField()

    def __str__(self):
        return f"Product({self.name})"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product-details", args=[str(self.id), ])
