#from django.db import migrations
from rest_framework import serializers
from sample.models import User, Posting, RidePosting


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'role']


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ['user', 'timePosted', 'category', 'prospective',
                  'fulfilled', 'description', 'audience']


class RidePostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RidePosting
        fields = ['posting', 'dateTimeOfRide', 'startLocation', 'endLocation',
                  'numberOfPeople']

