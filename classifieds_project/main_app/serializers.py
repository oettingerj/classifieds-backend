#from django.db import migrations
from rest_framework import serializers

from .models import ItemListing, RideListing, Location



class ItemListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemListing
        fields = ['id', 'created', 'title', 'description', 'user', 'img', 'price', 'sold']

class RideListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideListing
        fields = ['id', 'created', 'user', 'datetime', 'startLocation', 'endLocation', 'passengers', 'distance']


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
