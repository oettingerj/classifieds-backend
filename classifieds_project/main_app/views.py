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

# @api_view(['GET', 'POST'])
# def create_posting(request, user_pk, timePosted, category, prospective,
#                    fulfilled, description, audience):
#     """Creates a new posting object in the database using the given parameters"""
#
#     temp_dictionary = {
#         'user': user_pk,
#         'timePosted': timePosted,
#         'category': category,
#         'prospective': prospective,
#         'fulfilled': fulfilled,
#         'description': description,
#         'audience': audience
#     }
#     if request.method == "GET":
#         postings = Posting.objects.all()
#         serializer = PostingSerializer(postings, context={'request': request}, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         print("post method")
#         serializer = PostingSerializer(data=temp_dictionary)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #from here to **stopping point A** from master branch

    # temp_dictionary = {
    #     'name': name,
    #     'email': email,
    #     'role': role
    # }
    # serializer = UserSerializer(data=temp_dictionary)

    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #**stopping point A**


#@api_view(['GET', 'POST'])
#def create_posting(request, user_pk, timePosted, category, prospective,
#                   fulfilled, description, audience):
#    """Creates a new posting object in the database using the given parameters"""
#
#    temp_dictionary = {
#        'user': user_pk,
#        'timePosted': timePosted,
#        'category': category,
#        'prospective': prospective,
#        'fulfilled': fulfilled,
#        'description': description,
#        'audience': audience
#    }
#    if request.method == "GET":
#        postings = Posting.objects.all()
#        serializer = PostingSerializer(postings, context={'request': request}, many=True)
#        return Response(serializer.data)
#
#    elif request.method == "POST":
#        print("post method")
#        serializer = PostingSerializer(data=temp_dictionary)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_ridelisting(request, created, user, datetime, startLocation, endLocation, passengers, distance, sold):
    """ Creates a ride listing for the given parameters. """
    
    temp_dictionary = {
        'created': created,
        'user': user,
        'datetime': datetime,
        'startLocation': startLocation,
        'endLocation': endLocation,
        'passengers': passengers,
        'distance': distance,
        'sold': sold
    }
    
    if request.method == 'GET':
        ridelistings = RideListing.objects.all()
        serializer = RideListingSerializer(ridelistings, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RideListingSerializer(data=temp_dictionary)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def create_itemposting(request, posting_pk, images, price, forSale, forLoan):
#     """ Creates an item posting from the given parameters. One of these parameters is the primary key for the base
#     posting the item posting is connected to """
#
#     temp_dictionary = {
#         'posting': posting_pk,
#         # 'images': images, #intentionally excluded for importing test data
#         'price': price,
#         'forSale': forSale,
#         'forLoan': forLoan
#     }
#
#     if request.method == "GET":
#         postings = Posting.objects.all()
#         serializer = PostingSerializer(postings, context={'request': request}, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = ItemPostingSerializer(data=temp_dictionary)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def create_itemlisting(request, created, title, description, user, img, price, sold):
    """Creates an item listing for the given parameters"""
    temp_dictionary = {
        'created': created,
        'title': title,
        'description': description,
        'user': user,
        'img': img,
        'price': price,
        'sold': sold
    }

    if request.method == "GET":
        item_listings = ItemListing.objects.all()
        serializer = ItemListingSerializer(item_listings, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ItemListingSerializer(data=temp_dictionary)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def edit_ridelisting(request, pk, created, datetime, startLocation, endLocation, passengers, distance, sold):
    """ Edits a pre-existing database entry for a ride listing and updates it in place. """
    print("erl 1")
    post = RideListing.objects.get(pk=pk)
    print("erl 2")
    post.created = created
    post.user = request.user
    post.datetime = datetime
    post.startLocation = Location.objects.get(pk=startLocation)
    post.endLocation = Location.objects.get(pk=endLocation)
    post.passengers = passengers
    post.distance = distance
    post.sold = sold
    print("erl 3")
    post.save()
    print("erl 4")
    serializer = RideListingSerializer(post)
    print("erl 5")
#    serializer.save()
#    return Response(serializer.data)
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
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

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

@api_view(['GET','POST'])
def test01(request):
    return Response(request.user.email)
