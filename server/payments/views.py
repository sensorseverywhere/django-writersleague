import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView

from orders.models import Order
from .models import Customer
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
class CheckoutView(LoginRequiredMixin, TemplateView):
    model = Order
    template_name = 'payments/checkout.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)

        stripe_price = 100
        context['stripe_price'] = stripe_price
        context['publish_key'] = settings.STRIPE_PUBLISHABLE_KEY     

        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            print('Using dispatch method')
            # stripe_customer = stripe.Customer.create(email=request.user.email)
            charge = stripe.Charge.create(
                amount=500,
                currency='usd',
                description='Standard',
                source=request.POST['stripeToken']
            )

            return redirect(reverse('payments:success'))
        else:
            return super(CheckoutView, self).dispatch(request, *args, **kwargs)

# class PaymentSuccessView(LoginRequiredMixin, TemplateView):
#     print('paymentsuccessview')
#     template_name = 'account/dashboard.html'

def payment_success(request):
    if request.method == 'POST':
        return render(request, 'payments/checkout.html')
    else: 
        return render(request, 'payments/success.html')
