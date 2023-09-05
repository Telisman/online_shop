from django.contrib.sessions.models import Session
from django.shortcuts import render, get_object_or_404, redirect
from .models import ShoppingCart, CartItem
from shop_products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get the session key from the request's session
    session_key = request.session.session_key

    # Try to find an existing shopping cart associated with this session key
    try:
        cart = ShoppingCart.objects.get(session_id=session_key)
    except ShoppingCart.DoesNotExist:
        # If no cart is found, create a new one and associate it with the session
        cart = ShoppingCart(session_id=session_key)
        cart.save()

    # Create or retrieve the cart item for the product
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session = request.session
    cart = ShoppingCart.objects.get(session_id=session.session_key)
    cart_item = CartItem.objects.get(cart=cart, product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_view')

def cart_view(request):
    session_key = request.session.session_key
    cart = ShoppingCart.objects.get(session_id=session_key)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart_view.html', {'cart_items': cart_items})
