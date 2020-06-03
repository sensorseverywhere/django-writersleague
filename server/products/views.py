from django.views.generic import DetailView, ListView
from django.shortcuts import render

from .models import Product, Review
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
