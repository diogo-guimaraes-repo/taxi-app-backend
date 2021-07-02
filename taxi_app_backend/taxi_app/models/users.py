from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class BaseUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, unique=True, default="")
    birth_date = models.DateField()
    picture = models.ImageField(upload_to='uploads/% Y/% m/% d/')

    def __str__(self):
        return self.email


'''
class Client(AbstractUser):
    user = models.OneToOneField(
        BaseUser, on_delete=models.CASCADE, primary_key=True)
    credit = models.FloatField()
'''
