# Generated by Django 3.0.7 on 2020-07-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Voter'), (1, 'Author')], default=1),
        ),
    ]