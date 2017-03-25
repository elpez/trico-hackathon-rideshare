from __future__ import unicode_literals

from django.db import models

class DriverEvent(models.Model):
    name = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    date = models.DateTimeField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        date_str = self.date.strftime('%A %m/%d/%y at %I:%M %p')
        return '%s driving to %s, %s' % (self.name, self.destination, date_str)

class PassengerEvent(models.Model):
    name = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    date = models.DateTimeField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        date_str = self.date.strftime('%A %m/%d/%y at %I:%M %p')
        return '%s driving to %s, %s' % (self.name, self.destination, date_str)
