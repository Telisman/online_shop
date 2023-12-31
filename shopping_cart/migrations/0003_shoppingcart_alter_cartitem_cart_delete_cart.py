# Generated by Django 4.1.11 on 2023-09-05 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop_products", "0001_initial"),
        ("sessions", "0001_initial"),
        ("shopping_cart", "0002_cart_session"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShoppingCart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        through="shopping_cart.CartItem", to="shop_products.product"
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sessions.session",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="shopping_cart.shoppingcart",
            ),
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
    ]
