from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from .models import Order, OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart

import stripe
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration


stripe.api_key = "sk_test_owBhMcnDT8wl53B3jVGjf6SP00UgnKsLBG"


# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    qty=item['quantity']
                    )
            cart.clear()
            # send an email here confirming the order
            # start payment process
            request.session['order_id'] = str(order.id)
            return redirect(reverse('payments:checkout'))

        return
    else:
        form = CreateOrderForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})


# @staff_member_required
def admin_order_pdf(request, order_id):
    font_config = FontConfiguration()
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/pdf_invoice.html', {'order': order})
    print(html)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
    HTML(string=html).write_pdf(
        response,
        stylesheets=[CSS(settings.STATIC_ROOT + '/css/pdf.css')],
        font_config=font_config
        )
    return response
