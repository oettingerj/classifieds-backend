#from django.db import migrations
from rest_framework import serializers

from main_app.models import RideListing, ItemListing

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
