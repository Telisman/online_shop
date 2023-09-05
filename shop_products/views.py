from rest_framework import generics
from .serializers import ProductSerializer
from django.shortcuts import render, get_object_or_404
from .models import Product


# app product list
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})









# API BACKEND ENDPOINT VIEW FUNCTION
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
