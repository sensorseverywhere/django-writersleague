from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from orders.models import Order
from user.models import CustomUser
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
            self.update_votes(request.user, amount)
            return redirect(reverse('payments:success'))
        else:
            return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def update_votes(self, user, amount):
        with transaction.atomic():
            num_votes_qs = CustomUser.objects.select_for_update().filter(num_votes=user.num_votes)
            for votes in num_votes_qs:
                print(votes)
                votes.num_votes += amount / 10
                votes.save()


class PaymentSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'user/dashboard.html'
