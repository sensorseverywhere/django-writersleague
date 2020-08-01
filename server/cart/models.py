from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

from products.models import Product


class Cart(models.Model):
    OPEN = 10
    SUBMITTED = 20
    STATUSES = ((OPEN, "Open"), (SUBMITTED, "Submitted"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=OPEN)

    def is_empty(self):
        return self.lineitem_set.all().count() == 0

    def count(self):
        return sum(i.quantity for i in self.lineitem_set.all())

    def cart_total(self):
        return sum(i.quantity * i.product.price for i in self.lineitem_set.all())


class LineItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def get_lineitem_total(self):
        return self.product.price * self.quantity
