from django.urls import path
from . import views


urlpatterns = [
    path('api/products/', views.ProductList.as_view(), name='product-list'),
    path('api/products/<str:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/<str:product_id>/', views.product_detail, name='product_detail'),
]
