from decimal import Decimal

from django.conf import settings

from shop_app.models import Book


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # add product or update it's amount
    def add(self, product, quantity, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            if self.cart[product_id]['quantity'] + quantity <= Book.objects.filter(id=product_id).count():
                self.cart[product_id]['quantity'] += quantity
            else:
                pass
        self.save()

    def save(self):
        # update session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark session as 'changed' to make sure it was saved
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # get products from database
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Book.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # count all elements in cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    # delete cart from session
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
