import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView

from orders.models import Order
from user.models import CustomUser
from .models import Customer
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
class CheckoutView(LoginRequiredMixin, TemplateView):
    model = Order
    template_name = 'payments/checkout.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['publish_key'] = settings.STRIPE_PUBLISHABLE_KEY     
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            amount = int(float(request.POST['amount']))
            charge = stripe.Charge.create(
                amount=amount,
                currency='aud',
                description='Standard',
                source=request.POST['stripeToken']
            )

            votes = CustomUser.objects.filter(
                id=request.user.id
            ).update(num_votes=amount/10)

            return redirect(reverse('payments:success'))
        else:
            return super(CheckoutView, self).dispatch(request, *args, **kwargs)

class PaymentSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'user/dashboard.html'