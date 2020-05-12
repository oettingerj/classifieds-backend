#from django.db import migrations
from rest_framework import serializers
from auth_app.serializers import UserSerializer
from rest_framework.serializers import FloatField

from .models import ItemListing, RideListing, Location
from auth_app.models import User



class ItemListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemListing
        fields = ['id', 'created', 'user', 'title', 'description', 'img', 'price', 'sold', 'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        user_query_set = User.objects.filter(id=instance.user.id)
        representation['user'] = UserSerializer(user_query_set, many=True).data[0]
        
        return representation

class LocationSerializer(serializers.ModelSerializer):
    latitude = FloatField()
    longitude = FloatField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'latitude', 'longitude', 'address']

class RideListingSerializer(serializers.ModelSerializer):
    # distance = serializers.DecimalField(max_digits=12, decimal_places=8)

    class Meta:
        model = RideListing
        fields = ['id', 'created', 'user', 'datetime', 'startLocation', 'endLocation', 'passengers', 'sold']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        user_query_set = User.objects.filter(id=instance.user.id)
        representation['user'] = UserSerializer(user_query_set, many=True).data[0]

        start_location_query_set = Location.objects.filter(id=instance.startLocation.id)
        representation['startLocation'] = LocationSerializer(start_location_query_set, many=True).data[0]

        end_location_query_set = Location.objects.filter(id=instance.endLocation.id)
        representation['endLocation'] = LocationSerializer(end_location_query_set, many=True).data[0]

        return representation
