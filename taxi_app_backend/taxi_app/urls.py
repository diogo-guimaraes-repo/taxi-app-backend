from django.urls import include, path
from .views import ClientRegistrationView, DriverRegistrationView, DriverViewSet, ClientViewSet, TripViewSet, PaymentViewSet

from rest_framework import routers, views

app_name = 'taxi_app'

urlpatterns = [
    path('registration/client/', ClientRegistrationView.as_view(),
         name='register-client'),
    path('registration/driver/', DriverRegistrationView.as_view(),
         name='register-driver'),
    path('clients/', ClientViewSet.as_view()),
    path('drivers/', DriverViewSet.as_view())
]
