# Generated by Django 3.0.7 on 2020-08-12 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0004_auto_20200810_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStoryVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_votes', models.PositiveIntegerField(default=0)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('voter', 'story')},
            },
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]