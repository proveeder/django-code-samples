from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, product, cart, *args, **kwargs):
        self.product = product
        self.cart = cart
        super(CartAddProductForm, self).__init__(*args, **kwargs)

    def clean(self):
        quantity = self.cleaned_data['quantity']
        in_stock = self.cart.cart.get(str(self.product.id), {}).get("quantity", 0)
        if quantity + in_stock > self.product.amount:
            self.add_error("quantity", "too many books")
