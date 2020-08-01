from django import forms
from .models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'billing_name',
            'billing_address1',
            'billing_address2',
            'billing_post_code',
            'billing_city',
            'shipping_name',
            'shipping_address1',
            'shipping_address2',
            'shipping_post_code',
            'shipping_city'
            ]
