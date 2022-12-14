# Generated by Django 3.0.7 on 2020-11-26 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(10, 'New'), (20, 'Paid'), (30, 'Done')], default=10)),
                ('email', models.EmailField(max_length=254)),
                ('billing_name', models.CharField(max_length=60)),
                ('billing_address1', models.CharField(blank=True, max_length=250, null=True)),
                ('billing_address2', models.CharField(blank=True, max_length=250, null=True)),
                ('billing_post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_name', models.CharField(max_length=60)),
                ('shipping_address1', models.CharField(blank=True, max_length=250, null=True)),
                ('shipping_address2', models.CharField(blank=True, max_length=250, null=True)),
                ('shipping_post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('shipping_city', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statuses', models.IntegerField(choices=[(10, 'New'), (20, 'Processing'), (30, 'Sent'), (40, 'Cancelled')], default=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product')),
            ],
        ),
    ]
