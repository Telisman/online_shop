from rest_framework import generics
from .serializers import ProductSerializer
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q


# app product list

def product_list(request):
    # Get query parameters from the URL
    category = request.GET.get('category')
    query = request.GET.get('q')
    sort = request.GET.get('sort')

    # Start with all products
    products = Product.objects.all()

    # Apply category filter if specified
    if category:
        products = products.filter(category=category)

    # Apply search filter if a query is provided
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Apply sorting if specified
    if sort == 'asc':
        products = products.order_by('price')
    elif sort == 'desc':
        products = products.order_by('-price')

    return render(request, 'product_list.html', {
        'products': products,
        'selected_category': category,
        'search_query': query,
        'selected_sort': sort,
    })

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
