from django.conf import settings
from django.views.generic import DetailView, ListView

from .models import Plan, Product, Review
from cart.forms import CartAddProductForm


# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/all.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/single.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['update_quantity_form'] = CartAddProductForm()
        context['products'] = Product.objects.all()
        context['reviews'] = Review.objects.all()
        return context


class PlanListView(ListView):
    model = Plan
    context_object_name = 'plans'
    template_name = 'products/plans.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
