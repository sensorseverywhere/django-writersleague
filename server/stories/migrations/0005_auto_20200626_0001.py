# Generated by Django 3.0.7 on 2020-06-26 00:01

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20200623_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=models.TextField(),
        ),
    ]
