from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models.users import Client, Driver
from .models.trips import Trip, Payment
from .serializers.users import ClientRegisterSerializer, DriverRegisterSerializer, ClientSerializer, DriverSerializer
from .serializers.trips import TripSerializer, PaymentSerializer


class ClientRegistrationView(RegisterView):
    serializer_class = ClientRegisterSerializer


class DriverRegistrationView(RegisterView):
    serializer_class = DriverRegisterSerializer


class ClientViewSet(APIView):
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class DriverViewSet(APIView):
    def get(self, request, format=None):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
