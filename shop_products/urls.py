from django.urls import path
from .views import ProductList, ProductDetail,react_view

urlpatterns = [
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/products/<str:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('react/', react_view, name='react_view'),

]
