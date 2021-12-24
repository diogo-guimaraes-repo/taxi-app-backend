from django.db import models
from django.utils import timezone
from .users import Client, Driver


class Payment(models.Model):
    value = models.FloatField(default=50.0, blank=False)
    payment_time = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.payment_time = timezone.now()
        return super().save(*args, **kwargs)


class Trip(models.Model):

    class Status(models.TextChoices):
        PENDING_CONFIRMATION = "PENDING", "Pending"
        SCHEDULED = "SCHEDULED", "Scheduled"
        PICKUP = "PICKUP", "Pickup"
        IN_TRAVEL = "IN_TRAVEL", "In Travel"
        COMPLETE = "COMPLETE", "Complete"

    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    origin = models.CharField(max_length=200, blank=False)
    destination = models.CharField(max_length=200, blank=False)
    request_time = models.DateTimeField(editable=False)
    price = models.FloatField(default=0.0)
    trip_status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.PENDING_CONFIRMATION)

    def save(self, *args, **kwargs):
        if not self.id:
            self.request_time = timezone.now()
        return super().save(*args, **kwargs)
