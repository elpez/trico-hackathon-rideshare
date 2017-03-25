from __future__ import unicode_literals

from django.db import models

class DriverEvent(models.Model):
    name = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    time = models.TimeField()
    day = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return '%s driving to %s at %s %s' % (self.name, self.destination, self.day, self.time)

class PassengerEvent(models.Model):
    name = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    time = models.TimeField()
    day = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return '%s needs a ride to %s at %s %s' % (self.name, self.destination, self.day, self.time)
