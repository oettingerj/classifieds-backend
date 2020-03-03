#from django.db import migrations
from rest_framework import serializers

from sample.models import User, Posting, RidePosting, ItemPosting, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'role']


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
                  'numberOfPeople']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['posting', 'user', 'timePosted', 'content']
