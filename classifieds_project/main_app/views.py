# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render

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


@api_view(['GET','POST'])
def test01(request):
    print(request.COOKIES)
    print("test01 view called")
    print(request.user.email)
    #email_address = request.user.email

    return Response(request.user.email)

@api_view(['GET','POST'])
def test02(request):
    print("test02 view called")

    return Response(request.session)

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
def create_ridelisting(request, created, user, datetime, startLocation, endLocation, passengers, distance):
    """ Creates a ride listing for the given parameters. """
    
    temp_dictionary = {
        'created': created,
        'user': user,
        'datetime': datetime,
        'startLocation': startLocation,
        'endLocation': endLocation,
        'passengers': passengers,
        'distance': distance
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
        'description':description,
        'user':user,
        'img':img,
        'price': price,
        'sold':sold
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


def edit_ridelisting(request, created, user, datetime, startLocation, endLocation, passengers, distance):
    """ Edits a pre-existing database entry for a ride listing and updates it in place. """
    
    post = RideLists.objects.get(pk=request.kwargs['pk'])
    
    post.created = created
    post.user = user
    post.datetime = datetime
    post.startLocation = startLocation
    post.endLocation = endLocation
    post.passengers = passengers
    post.distance = distance
    
    serializer = PostListingSerializer(post)
    serializer.save()
    return Response(serializer.data)


def edit_itemlisting(request, created, title, description, user, img, price, sold):
    """Edits a pre-existing database entry for an item posting and updates it in place. """

    post = ItemListing.objects.get(pk=request.kwargs['pk'])
    # use is_valid?
    post.created = created
    post.description = description
    post.title = title
    post.user = user # probs not necessary
    post.img = img
    post.price = price
    post.sold = sold
    post.save()
    serializer = ItemListingSerializer(post)
    return Response(serializer.data)  # not sure if this is best way to do thsi


def delete_ridelisting(request):
    """ Deletes the ride listing associated with the given primary key from the database. """
    
    post = RideListing.objects.get(pk=request.kwargs['pk'])
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def delete_itemlisting(request):
    """Deletes the item posting associated with the given primary key from the database"""
    post = ItemListing.objects.get(pk=request.kwargs['pk'])
    post.delete()
    return render(request, 'sample/posting_list.html')  # replace HTML File


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

        #test_query_set = User.objects
        #serializer = UserSerializer(test_query_set, many=True)

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


def search_postings(request, keyword):
    """Returns all database entries whose 'description' field includes the given keyword. """

    posting_list = ItemListing.objects.filter(description__contains=keyword)  # is this the filter we want?
    serializer = ItemListingSerializer(posting_list, context={'request': request}, many=True)
    return Response(serializer.data)

def toggle_ridelisting_sold(request):
    """Toggles between 'sold' values for a given post; if the post was marked as 'sold' it is now marked as
    'sold', and vice versa """

    post = RideListing.objects.get(pk=request.kwargs['pk'])
    if post.sold:
        post.sold = False
    else:
        post.sold = True
    post.save()
    return render(request, 'sample/posting_list.html')  # replace HTML File


def toggle_itemlisting_sold(request):
    """Toggles between 'sold' values for a given post; if the post was marked as 'sold' it is now marked as
    'sold', and vice versa """

    post = ItemListing.objects.get(pk=request.kwargs['pk'])
    if post.sold:
        post.sold = False
    else:
        post.sold = True
    post.save()
    return render(request, 'sample/posting_list.html')  # replace HTML File


def view_ridelisting_details(request):
    """Returns all information associated with the post with the given primary key. """

    post = RideListing.objects.get(pk=request.kwargs['pk'])
    serializer = RideListingSerializer(post, context={'request': request}, many=True)
    return Response(serializer.data)


def view_itemlisting_details(request):
    """Returns all information associated with the post with the given primary key. """

    post = ItemListing.objects.get(pk=request.kwargs['pk'])
    serializer = ItemListingSerializer(post, context={'request': request}, many=True)
    return Response(serializer.data)


def save_ridelisting(request, user_pk):
    """ Adds a ride listing to a user's collection of saved rides, and adds that user to the ride listing's collection of users that have saved it. """
    
    post = RideListing.objects.get(pk=request.kwargs['pk'])
    user = User.objects.get(pk=user_pk)
    post.savedBy.add(user)
    serializer = RideListingSerializer(post, context={'request': request}, many=True)
    serializer.save()
    return Response(serializer.data)


def save_itemlisting(request, user_pk):
    """ Adds an item listing to a user's collection of saved items, and adds that user to the item listing's collection of users that have saved it. """
    
    post = ItemListing.objects.get(pk=request.kwargs['pk'])
    user = User.objects.get(pk=user_pk)
    post.savedBy.add(user)
    serializer = ItemListingSerializer(post, context={'request': request}, many=True)
    serializer.save()
    return Response(serializer.data)


def unsave_ridelisting(request, user_pk):
    """ Removes a ride listing from a user's collection of saved rides, and removes that user from the ride listing's collection of users that have saved it. """
    
    post = RideListing.objects.get(pk=request.kwargs['pk'])
    user = User.objects.get(pk=user_pk)
    post.savedBy.remove(user)
    post.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


def unsave_itemlisting(request, user_pk):
    """ Removes an item listing from a user's collection of saved items, and removes that user from the item listing's collection of users that have saved it. """
    
    post = ItemListing.objects.get(pk=request.kwargs['pk'])
    user = User.objects.get(pk=user_pk)
    post.savedBy.remove(user)
    post.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


def display_saved_ridelistings(request, user_pk):
    """ Displays the ride listings that the given user has saved. """
    
    user = User.objects.get(pk=user_pk)
    posts = user.savedRides.all()
    serializer = RideListingSerializer(posts, many=True)
    return Response(serializer.data)


def display_saved_itemlistings(request, user_pk):
    """ Displays the item listings that the given user has saved. """
    
    user = User.objects.get(pk=user_pk)
    posts = user.savedItems.all()
    serializer = ItemListingSerializer(posts, many=True)
    return Response(serializer.data)
