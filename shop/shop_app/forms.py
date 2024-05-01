from django import forms


class BookForm(forms.Form):
    name = forms.CharField(label='Your first and last name', required=True)
    email = forms.CharField(label='Your email', required=True)
