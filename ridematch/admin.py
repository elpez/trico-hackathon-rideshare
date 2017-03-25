from django.contrib import admin

from .models import DriverEvent, PassengerEvent

admin.site.register(DriverEvent)
admin.site.register(PassengerEvent)
