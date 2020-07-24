from django.db import models
from user.models import CustomUser

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=True)