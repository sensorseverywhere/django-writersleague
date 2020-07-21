from django.contrib.auth.models import ( AbstractUser, BaseUserManager, )
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set.")
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(email=email)

class CustomUser(AbstractUser):
    SPONSOR = 0
    AUTHOR = 1
    USER_TYPES = (
        (SPONSOR, 'Sponsor'),
        (AUTHOR, 'Author')
    )
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField('email address', unique=True)
    user_type = models.IntegerField(choices=USER_TYPES, default=AUTHOR)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def natural_key(self):
        return (self.email)

class Guest(models.Model):
    email = models.EmailField('email address')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


class Address(models.Model):
    SUPPORTED_COUNTRIES = (
        ("au", "Australia"),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    address1 = models.CharField("Address line 1", max_length=60)
    address2 = models.CharField("Address line 2", max_length=60, blank=True)
    post_code = models.CharField("Postcode", max_length=4)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=3, choices=SUPPORTED_COUNTRIES)

    def __str__(self):
        return ", ".join(
            [
                self.name, 
                self.address1,
                self.address2,
                self.post_code,
                self.city,
                self.country,
            ]
        )