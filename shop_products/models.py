from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    image_urls = models.JSONField()  # Store image URLs as a JSON array

    def __str__(self):
        return self.name
