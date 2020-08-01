import random
import os
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(filename='DEFAULT', file_path='', *args, **kwargs):
    filename_hash = random.randint(1, 34582345)
    name, ext = get_filename_ext(filename)
    new_filename = '{filename_hash}{ext}'.format(filename_hash=filename_hash, ext=ext)
    if file_path == 'main':
        return "products/main/{new_filename}".format(
            new_filename=new_filename
            )
    else:
        return "products/thumbs/{new_filename}".format(
            new_filename=new_filename
            )


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    sku = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=48)
    stock_qty = models.IntegerField()
    active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Product._meta.fields]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])

    def get_by_natural_key(self, name):
        return self.get(name=name)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/main')
    thumbnail = models.ImageField(upload_to='products/thumbs')
    # image = models.ImageField(upload_to=upload_image_path(file_path='main'))
    # thumbnail = models.ImageField(upload_to=upload_image_path(file_path='thumbs'))


class Plan(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    requires_subscription = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name)


class Category(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.product.name
