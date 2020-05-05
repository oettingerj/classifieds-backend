# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
  
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status


#note: if this doesn't work:
#   from django.conf import settings
#   User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import User

from .models import Posting, RidePosting, ItemPosting
from .serializers import *


@api_view(['GET', 'POST'])
def create_posting(request, user_pk, timePosted, category, prospective,
                   fulfilled, description, audience):
    """Creates a new posting object in the database using the given parameters"""

    temp_dictionary = {
        'user': user_pk,
        'timePosted': timePosted,
        'category': category,
        'prospective': prospective,
        'fulfilled': fulfilled,
        'description': description,
        'audience': audience
    }
    if request.method == "GET":
        postings = Posting.objects.all()
        serializer = PostingSerializer(postings, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        print("post method")
        serializer = PostingSerializer(data=temp_dictionary)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_rideposting(request, posting_pk, dateTimeOfRide, startLocation, endLocation, numberOfPeople, willingToPay, payment):
    """ Creates an ride posting from the given parameters. One of these parameters is the primary key for the base
    posting the ride posting is connected to """

    temp_dictionary = {
        'posting': posting_pk,
        'dateTimeOfRide': dateTimeOfRide,
        'startLocation': startLocation,
        'endLocation': endLocation,
        'numberOfPeople': numberOfPeople,
        'willingToPay': willingToPay,
        'payment': payment
        }

    serializer = RidePostingSerializer(data=temp_dictionary)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_itemposting(request, posting_pk, images, price, forSale, forLoan):
    """ Creates an item posting from the given parameters. One of these parameters is the primary key for the base
    posting the item posting is connected to """

    temp_dictionary = {
        'posting': posting_pk,
        # 'images': images, #intentionally excluded for importing test data
        'price': price,
        'forSale': forSale,
        'forLoan': forLoan
    }

    if request.method == "GET":
        postings = Posting.objects.all()
        serializer = PostingSerializer(postings, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ItemPostingSerializer(data=temp_dictionary)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def edit_rideposting(request, ride_pk, posting_pk, dateTimeOfRide, startLocation, endLocation, numberOfPeople, willingToPay, payment):
    """Edits a pre-existing database entry for a ride posting and updates it in place. """
    rideposting = RidePosting.objects.get(pk=ride_pk)
    rideposting.dateTimeOfRide = dateTimeOfRide
    rideposting.startLocation = startLocation
    rideposting.endLocation = endLocation
    rideposting.numberOfPeople = numberOfPeople
    rideposting.willingToPay = willingToPay
    rideposting.payment = payment
    rideposting.save()
    serializer = RidePostingSerializer(rideposting)
    return Response(serializer.data)


def edit_itemposting(request, item_pk, posting_pk, images, price, forSale, forLoan):
    """Edits a pre-existing database entry for an item posting and updates it in place. """

    post = ItemPosting.objects.get(pk=item_pk)
    # use is_valid?
    post.images = images
    post.price = price
    post.forSale = forSale
    post.forLoan = forLoan
    post.save()
    serializer = ItemPostingSerializer(post)
    return Response(serializer.data)  # not sure if this is best way to do thsi


def delete_rideposting(request, key):
    """Deletes the ride posting associated with the given primary key from the database"""
    rideposting = RidePosting.objects.get(pk=key)
    rideposting.delete()
    return render(request, 'sample/posting_list.html')


def delete_itemposting(request, item_pk):
    """Deletes the item posting associated with the given primary key from the database"""
    post = ItemPosting.objects.get(pk=item_pk)
    post.delete()
    return render(request, 'sample/posting_list.html')  # replace HTML File


@api_view(['GET'])
def get_available_postings(request, category):
    """Returns all available postings in a given category. If no category is given, return all postings."""
    current_user = request.user
    current_user_role = current_user.role

    query_set = ''
    if category == '':
        query_set = Posting.objects.filter(user__role=current_user_role)
    else:
        query_set = Posting.objects.filter(user__role=current_user_role, category=category)
    serializer = PostingSerializer(query_set, many=True)
    json = JSONRenderer().render(serializer.data)

    #return Response(json)
    return Response(serializer.data) #debug so returns JSON successfully

@api_view(['GET'])
def get_own_postings(request):
    """Returns all postings attributed to a given User. """
    current_user = request.user
    query_set = Posting.objects.filter(user=current_user)

    serializer = PostingSerializer(query_set, many=True)
    json = JSONRenderer().render(serializer.data)

    #return Response(json)
    return Response(serializer.data) #debug so returns JSON successfully


def search_postings(request, keyword):
    """Returns all database entries whose 'description' field includes the given keyword. """

    postingList = Posting.objects.filter(description__contains=keyword)  # is this the filter we want?
    serializer = PostingSerializer(postingList, context={'request': request}, many=True)
    return Response(serializer.data)


def toggle_posting_fulfilled(request, pk):
    """Toggles between 'fulfilled' values for a given post; if the post was marked as 'unfulfilled' it is now marked as
    'fulfilled', and vice versa """

    post = Posting.objects.get(pk=pk)
    if post.fulfilled:
        post.fulfilled = False
    else:
        post.fulfilled = True
    post.save()
    return render(request, 'sample/posting_list.html')  # replace HTML File




def view_posting_details(request, pk):
    """Returns all information associated with the post with the given primary key. """

    # do we need one of these for item/ride as well?
    post = Posting.objects.get(pk=pk)
    serializer = PostingSerializer(post, context={'request': request}, many=True)
    return Response(serializer.data)


def save_posting(request, posting_pk, user_pk):
    """Adds a posting to a user's collection of saved postings, and adds that user to the posting's collection of users that have saved it."""
    
    post = Posting.objects.get(pk=posting_pk)
    user = User.objects.get(pk=user_pk)
    post.savedBy.add(user)
    post.save()
    return render(request, 'sample/posting_list.html') #change this
    
    
def unsave_posting(request, posting_pk, user_pk):
    """Removes a posting from a user's collection of saved postings, and removes that user from the posting's collection of users that have saved it."""
    
    post = Posting.objects.get(pk=posting_pk)
    user = User.objects.get(pk=user_pk)
    post.savedBy.remove(user)
    post.save()
    return render(request, 'sample/posting_list.html') #change this


def display_saved_postings(request, user_pk):
    """Displays the postings that the given user has saved."""
    
    user = User.objects.get(pk=user_pk)
    postings = user.savedPostings.all()
#    serializer = PostingSerializer(postings, many=True)
#    return Response(serializer.data)
    return render(request, 'sample/posting_list.html', {'postings': postings}) #change this
    

# #USERS
# @api_view(['POST'])
# def create_user(request, name, email, role):
