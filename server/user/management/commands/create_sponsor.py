import os
from django.core.management.base import BaseCommand
from user.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
            CustomUser.objects.create_user('sponsor@writersleague.com', 'Qqqqqq!1')