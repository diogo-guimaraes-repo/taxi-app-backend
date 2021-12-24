from django.contrib import admin
from .models import BaseUser, Client, Driver, Admin, Payment, Trip

# Register your models here.
admin.site.register(BaseUser)
admin.site.register(Client)
admin.site.register(Driver)
admin.site.register(Admin)
admin.site.register(Payment)
admin.site.register(Trip)
