import uuid

from django.conf import settings
from django.db import models

from products.models import Product


# Create your models here.
class Order(models.Model):
    """
        Billing and shipping info for the order
    """
    NEW = 10
    PAID = 20
    DONE = 30

    STATUSES = (
        (NEW, "New"),
        (PAID, "Paid"),
        (DONE, "Done")
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=NEW)
    email = models.EmailField()

    billing_name = models.CharField(max_length=60)
    billing_address1 = models.CharField(max_length=250, blank=True, null=True)
    billing_address2 = models.CharField(max_length=250, blank=True, null=True)
    billing_post_code = models.CharField(max_length=20, blank=True, null=True)
    billing_city = models.CharField(max_length=100, blank=True, null=True)

    shipping_name = models.CharField(max_length=60)
    shipping_address1 = models.CharField(max_length=250, blank=True, null=True)
    shipping_address2 = models.CharField(max_length=250, blank=True, null=True)
    shipping_post_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """
        Product info for the order
    """
    NEW = 10
    PROCESSING = 20
    SENT = 30
    CANCELLED = 40

    STATUSES = (
        (NEW, "New"),
        (PROCESSING, "Processing"),
        (SENT, "Sent"),
        (CANCELLED, "Cancelled")
        )

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    statuses = models.IntegerField(choices=STATUSES, default=NEW)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.qty
