from rest_framework import serializers

from ..models import Client, Driver, Admin, Trip, Payment
from .users import ClientSerializer, DriverSerializer


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('value', 'payment_time')


class TripSerializer(serializers.ModelSerializer):
    client = ClientSerializer
    driver = DriverSerializer
    payment = PaymentSerializer

    class Meta:
        model = Trip
        fields = ('origin', 'destination',
                  'request_time', 'price', 'trip_status')
