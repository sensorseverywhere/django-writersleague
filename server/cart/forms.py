from django import forms
from django.forms import inlineformset_factory
from .models import Cart, LineItem

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

LineItemFormSet = inlineformset_factory(
    Cart,
    LineItem,
    fields=("quantity",),
    extra=0,
)


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
