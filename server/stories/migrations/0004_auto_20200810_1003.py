# Generated by Django 3.0.7 on 2020-08-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.SmallIntegerField(choices=[(1, '🔺'), (-1, '🔻')]),
        ),
    ]
