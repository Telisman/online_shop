from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# views.py

from django.shortcuts import render

def react_view(request):
    return render(request, 'index.html')


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
