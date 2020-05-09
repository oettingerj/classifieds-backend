
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser
)
from django.db import models
from datetime import datetime
# from .serializers import (
#     UserSerializer, 
#     AuthBackendSerializer, 
#     PostingSerializer, 
#     ItemPostingSerializer, 
#     RidePostingSerializer
# )
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response




class User(models.Model):
    #id implicitly created
    name = models.CharField(max_length=240)
    email = models.CharField(max_length=120)

    roleChoice = models.TextChoices('roleChoice', 'STUDENT FACULTY STAFF ALL')
    type = models.CharField(choices=roleChoice.choices, max_length=7)


    def __str__(self):
        return self.name


class ItemListing(models.Model):
    #id implicitly created
    created = models.DateTimeField()
    title = models.CharField(max_length=240)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='poster', on_delete=models.CASCADE)
    img = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sold = models.BooleanField()
    savedBy = models.ManyToManyField(User, related_name='savedItems')

class Location(models.Model):
    #id implicitly created
    name = models.CharField(max_length=240)
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)
    address = models.TextField()

class RideListing(models.Model):
    #id implicitly created
    created = models.DateTimeField()
    user = models.ForeignKey(User, related_name='ride_offerer', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    startLocation = models.ForeignKey(Location, related_name='start_location', on_delete=models.CASCADE)
    endLocation = models.ForeignKey(Location, related_name='end_location', on_delete=models.CASCADE)
    passengers = models.IntegerField()
    distance = models.DecimalField(max_digits=12, decimal_places=8),
    savedBy = models.ManyToManyField(User, related_name='savedRides')



