from django.db import models
from datetime import datetime
from django.conf import settings

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class ItemListing(models.Model):
    #id implicitly created
    created = models.DateTimeField()
    title = models.CharField(max_length=240)
    description = models.TextField()
    category = models.CharField(max_length=120,default="not specified")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='poster', on_delete=models.CASCADE)
    img = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sold = models.BooleanField()
    savedBy = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='savedItems')

class Location(models.Model):
    #id implicitly created
    name = models.CharField(max_length=240)
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    address = models.TextField()

class RideListing(models.Model):
    #id implicitly created
    created = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ride_offerer', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    startLocation = models.ForeignKey(Location, related_name='start_location', on_delete=models.CASCADE)
    endLocation = models.ForeignKey(Location, related_name='end_location', on_delete=models.CASCADE)
    passengers = models.IntegerField()
    distance = models.DecimalField(max_digits=12, decimal_places=8),
    savedBy = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='savedRides')
    sold = models.BooleanField()



