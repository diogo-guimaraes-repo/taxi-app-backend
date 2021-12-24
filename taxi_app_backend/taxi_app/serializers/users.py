from typing_extensions import Required
from django.db.models import fields
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from ..models import BaseUser, Client, Driver, Admin


class ClientRegisterSerializer(RegisterSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True,)
    phone_number = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(ClientRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'phone_number': self.validated_data.get('phone_number', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(ClientRegisterSerializer, self).save(request)
        user.user_type = BaseUser.Types.CLIENT
        user.save()
        client = Client(
            client=user, phone_number=self.cleaned_data.get('phone_number'))
        client.save()
        return user


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['first_name', 'last_name', 'email',
                  'birth_date', 'picture', 'user_type']


class ClientSerializer(serializers.ModelSerializer):
    client = BaseUserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'credit', 'phone_number', 'client']


class DriverSerializer(serializers.ModelSerializer):
    driver = BaseUserSerializer(read_only=True)

    class Meta:
        model = Driver
        fields = ['rating', 'phone_number', 'driver']


class DriverRegisterSerializer(RegisterSerializer):
    driver = serializers.PrimaryKeyRelatedField(read_only=True,)
    phone_number = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(DriverRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'phone_number': self.validated_data.get('phone_number', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(DriverRegisterSerializer, self).save(request)
        user.user_type = BaseUser.Types.DRIVER
        user.save()
        driver = Driver(
            driver=user, phone_number=self.cleaned_data.get('phone_number'))
        driver.save()
        return user
