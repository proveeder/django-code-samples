from django.shortcuts import get_object_or_404, redirect, render

from shop_app.models import Book

from .cart import Cart


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove(product)

    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)

    return render(request, 'cart/cart_detail.html', {'cart': cart})
