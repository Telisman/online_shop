from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
]
