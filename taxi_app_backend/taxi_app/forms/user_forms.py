from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from models.users import BaseUser


class BaseUserCreationForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('first_name', 'last_name', 'email')
