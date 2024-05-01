from cart.cart import Cart

from django.shortcuts import render

from shop_app.models import Book

from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import send_mail, send_to_api


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                # change book amount
                book = Book.objects.get(name=item['product'].name)
                book.amount -= item['quantity']
                book.save()

                # send changes to warehouse
                send_to_api(name=item['product'].name)

            # send success message
            send_mail.delay(order.id)

            # clear cart
            cart.clear()

            return render(request, 'orders/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order_create.html',
                  {'cart': cart, 'form': form})
