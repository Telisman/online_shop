from django.urls import path
from . import views

urlpatterns = [

    path('api/cart/', views.CartView.as_view(), name='product-list'),
    path('api/cart/add/<str:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('api/cart/remove/<str:product_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),



    path('add_to_cart/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
]
