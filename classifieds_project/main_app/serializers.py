#from django.db import migrations
from rest_framework import serializers
from auth_app.serializers import UserSerializer

from .models import ItemListing, RideListing, Location
from auth_app.models import User



class ItemListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemListing
        fields = ['id', 'created', 'user', 'title', 'description', 'img', 'price', 'sold']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        user_query_set = User.objects.filter(id=instance.user.id)
        representation['user'] = UserSerializer(user_query_set, many=True).data[0]
        
        return representation



class RideListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideListing
        fields = ['id', 'created', 'user', 'datetime', 'startLocation', 'endLocation', 'passengers', 'distance']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        user_query_set = User.objects.filter(id=instance.user.id)
        representation['user'] = UserSerializer(user_query_set, many=True).data[0]
        
        return representation
