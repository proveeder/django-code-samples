from cart.cart import Cart
from cart.forms import CartAddProductForm

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView

from .models import Book


def startpage(request):
    return HttpResponse("You are on the startpage")


class BookListView(ListView):
    model = Book
    template_name = 'book/books_list.html'


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    cart = Cart(request)
    form = CartAddProductForm(product=book, cart=cart)

    if request.method == 'POST':
        form = CartAddProductForm(data=request.POST, product=book, cart=cart)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=book,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
            return redirect('cart_detail')

    return render(request, 'book/book_detail.html', {'product': book,
                                                     'cart_product_form': form})
