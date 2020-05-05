#from django.db import migrations
from rest_framework import serializers

from .models import Posting, RidePosting, ItemPosting


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role']

# class AuthBackendSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuthBackend
#         fields = []


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ['user', 'timePosted', 'category', 'prospective',
                  'fulfilled', 'description', 'audience']


class ItemPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPosting
        fields = ['posting', 'images', 'price', 'forSale', 'forLoan']


class RidePostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RidePosting
        fields = ['posting', 'dateTimeOfRide', 'startLocation', 'endLocation',
                  'numberOfPeople', 'willingToPay', 'payment']

