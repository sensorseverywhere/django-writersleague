# Generated by Django 3.0.7 on 2020-08-12 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20200812_0325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstoryvotes',
            old_name='num_votes',
            new_name='votes',
        ),
    ]
