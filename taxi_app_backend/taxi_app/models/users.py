from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class BaseUser(AbstractUser):

    ROLE_CHOICES = (
        (1, "client"),
        (2, "driver"),
        (3, "admin"),
    )

    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address")
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, unique=True, default="")
    birth_date = models.DateField()
    picture = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    credit = models.FloatField(default=0.00)
    user_type = models.IntegerField(
        choices=ROLE_CHOICES, default=1)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.email
