from django.urls import path 

from .views import CheckoutView, payment_success

app_name = 'payments'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('success/', payment_success, name='success'),
]