# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer


#note: if this doesn't work:
#   from django.conf import settings
#   User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import User

from .models import ItemListing, RideListing, Location
from .serializers import *

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect


from rest_framework.authentication import SessionAuthentication, BasicAuthentication



@api_view(['POST'])
def create_ridelisting(request):
    """ Creates a ride listing for the given parameters. """

    body_params = request.data

    start_loc_serializer = LocationSerializer(data=body_params.get('startLocation'))
    end_loc_serializer = LocationSerializer(data=body_params.get('endLocation'))
    if start_loc_serializer.is_valid() and end_loc_serializer.is_valid():
        start_id = start_loc_serializer.save().id
        end_id = end_loc_serializer.save().id
    else:
        return Response(start_loc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    temp_dictionary = {
        'created': body_params.get('created'),
        'user': request.user.id,
        'datetime': body_params.get('datetime'),
        'startLocation': start_id,
        'endLocation': end_id,
        'passengers': body_params.get('passengers'),
        'distance': body_params.get('distance'),
        'sold': False
    }
    
    serializer = RideListingSerializer(data=temp_dictionary)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def create_itemlisting(request):
    """Creates an item listing for the given parameters"""
    body_params = request.data

    temp_dictionary = {
        'created': body_params.get('created'),
        'title': body_params.get('title'),
        'description': body_params.get('description'),
        'user': request.user.id,
        'img': body_params.get('img'),
        'price': body_params.get('price'),
        'sold': False
    }

    serializer = ItemListingSerializer(data=temp_dictionary)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def edit_ridelisting(request, pk, created, datetime, startLocation, endLocation, passengers, distance, sold):
    """ Edits a pre-existing database entry for a ride listing and updates it in place. """

    post = RideListing.objects.get(pk=pk)
    post.created = created
    post.datetime = datetime
    post.startLocation = Location.objects.get(pk=startLocation)
    post.endLocation = Location.objects.get(pk=endLocation)
    post.passengers = passengers
    post.distance = distance
    post.sold = sold
    post.save()
    serializer = RideListingSerializer(post)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def edit_itemlisting(request, pk, created, title, description, user, img, price, sold):
    """Edits a pre-existing database entry for an item posting and updates it in place. """

    post = ItemListing.objects.get(pk=pk)
    post.created = created
    post.description = description
    post.title = title
    post.user = request.user
    post.img = img
    post.price = price
    post.sold = sold
    post.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def delete_ridelisting(request, pk):
    """ Deletes the ride listing associated with the given primary key from the database. """
    
    post = RideListing.objects.get(pk=pk)
    if post.user == request.user:
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

    
@api_view(['POST'])
def delete_itemlisting(request, pk):
    """Deletes the item posting associated with the given primary key from the database"""
    post = ItemListing.objects.get(pk=pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_available_postings(request, category):
    """Returns all available postings in a given category. If no category is given, return all postings."""
    if request.user.is_authenticated:
        current_user = request.user
        current_user_role = current_user.role

        query_set = ''
        if category == '':
            query_set = ItemListing.objects
        else:
            query_set = ItemListing.objects.filter(category=category)
        serializer = ItemListingSerializer(query_set, many=True)

        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

    
@api_view(['GET'])
def get_available_rides(request):
    """Returns all available postings in a given category. If no category is given, return all postings."""
    if request.user.is_authenticated:
        serializer = RideListingSerializer(RideListing.objects, many=True)

        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

    
@api_view(['GET'])
def get_own_postings(request):
    """Returns all postings attributed to a given User. """
    if request.user.is_authenticated:
        current_user = request.user
        query_set = ItemListing.objects.filter(user=current_user)

        serializer = ItemListingSerializer(query_set, many=True)

        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

    
@api_view(['GET'])
def search_postings(request, keyword):
    """Returns all database entries whose 'description' or 'title' field includes the given keyword. """

    query_set = ItemListing.objects.filter(Q(description__icontains=keyword) | Q(title__icontains=keyword))
    print(len(query_set))
    serializer = ItemListingSerializer(query_set, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def change_ridelisting_sold(request, pk, new_sold):
    """Toggles between 'sold' values for a given post; if the post was marked as 'sold' it is now marked as
    'sold', and vice versa """

    post = RideListing.objects.get(pk=pk)
    post.sold = new_sold
    post.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def change_itemlisting_sold(request, pk, new_sold):
    """Toggles between 'sold' values for a given post; if the post was marked as 'sold' it is now marked as
    'sold', and vice versa """

    post = ItemListing.objects.get(pk=pk)
    post.sold = new_sold
    post.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def view_ridelisting_details(request, pk):
    """Returns all information associated with the post with the given primary key. """

    post = RideListing.objects.get(pk=pk)
    serializer = RideListingSerializer(post, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def view_itemlisting_details(request, pk):
    """Returns all information associated with the post with the given primary key. """
    post = ItemListing.objects.get(pk=pk)
    serializer = ItemListingSerializer(post, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
def like_ridelisting(request, pk):
    """ Adds a ride listing to a user's collection of liked rides, and adds that user to the ride listing's collection of users that have liked it. """
    
    post = RideListing.objects.get(pk=pk)
    user = request.user
    post.likedBy.add(user)
    post.save()
    serializer = RideListingSerializer(post, context={'request': request}, many=True)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def like_itemlisting(request, pk):
    """ Adds an item listing to a user's collection of liked items, and adds that user to the item listing's collection of users that have liked it. """
    
    post = ItemListing.objects.get(pk=pk)
    user = request.user
    post.likedBy.add(user)
    post.save()
    serializer = ItemListingSerializer(post, context={'request': request}, many=True)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def unlike_ridelisting(request, pk):
    """ Removes a ride listing from a user's collection of liked rides, and removes that user from the ride listing's collection of users that have liked it. """
    
    post = RideListing.objects.get(pk=pk)
    user = request.user
    post.likedBy.remove(user)
    post.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def unlike_itemlisting(request, pk):
    """ Removes an item listing from a user's collection of liked items, and removes that user from the item listing's collection of users that have liked it. """
    
    post = ItemListing.objects.get(pk=pk)
    user = request.user
    post.likedBy.remove(user)
    post.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def display_liked_ridelistings(request):
    """ Displays the ride listings that the given user has liked. """
    
    user = request.user
    posts = user.likedRides.all()
    serializer = RideListingSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def display_liked_itemlistings(request):
    """ Displays the item listings that the given user has liked. """
    
    user = request.user
    posts = user.likedItems.all()
    serializer = ItemListingSerializer(posts, many=True)
    return Response(serializer.data)