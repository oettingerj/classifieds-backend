#from django.db import migrations
from rest_framework import serializers

from .models import User, ItemListing, Location, RideListing


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role']

class AuthBackendSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthBackend
        fields = []



class ItemListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemListing
        fields = ['created', 'title', 'description', 'user', 'img', 'price', 'sold']

class RideListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideListing
        fields = ['created', 'user', 'datetime', 'startLocation', 'endLocation', 'passengers', 'distance']


# class ItemPostingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ItemListing
#         fields = ['created', 'title', 'description', 'user', 'img', 'price', 'sold']
#
#
# class RidePostingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RideListing
#         fields = ['created','user','datetime','startLocation','endLocation','passengers','distance']
