from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.conf import settings


class BaseUser(AbstractUser):

    class Types(models.TextChoices):
        CLIENT = "CLIENT", "Client"
        DRIVER = "DRIVER", "Driver"
        ADMIN = "ADMIN", "Admin"

    base_type = Types.CLIENT
    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address")
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='uploads/% Y/% m/% d/', blank=True)
    user_type = models.CharField(
        max_length=50, choices=Types.choices, default=base_type)
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"


class Client(models.Model):
    client = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    credit = models.FloatField(default=0.00)
    base_type = BaseUser.Types.CLIENT
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=False, unique=True, default="")

    def __str__(self):
        return self.client.username


class Driver(models.Model):
    driver = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.FloatField(default=0.00)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=False, unique=True, default="")
    base_type = BaseUser.Types.DRIVER

    def __str__(self):
        return self.driver.username


class Admin(models.Model):
    admin = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=False, unique=True, default="")
    base_type = BaseUser.Types.ADMIN

    def __str__(self):
        return self.admin.username
