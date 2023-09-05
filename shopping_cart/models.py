from django.db import models
from django.contrib.sessions.models import Session
from shop_products.models import Product

class ShoppingCart(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
