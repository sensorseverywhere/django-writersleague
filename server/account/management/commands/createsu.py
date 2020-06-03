import os
from django.core.management.base import BaseCommand
from account.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
            print(os.environ.get('SUPERUSER_EMAIL'))
            CustomUser.objects.create_superuser(os.environ.get('SUPERUSER_EMAIL'), os.environ.get('SUPERUSER_PASS'))
