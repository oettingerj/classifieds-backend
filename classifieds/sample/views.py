# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
  
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status

from django.contrib.auth.models import User

from .models import User, Posting, RidePosting, ItemPosting
from .serializers import *


@api_view(['GET', 'POST'])
def import_user(request, name, email, role):

    temp_dictionary = {
        'name': name, 
        'email': email, 
        'role': role
    }
    serializer = UserSerializer(data=temp_dictionary)
   
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def import_posting(request, user_pk, timePosted, category, prospective, 
                   fulfilled, description, audience):
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

    
@api_view(['GET','POST'])
def import_itemPosting(request, posting_pk, images, price, forSale, forLoan):
    temp_dictionary = {
        'posting': posting_pk,
        #'images': images, #intentionally excluded for importing test data
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


@api_view(['GET', 'POST'])
def create_rideposting(request, posting_pk, dateTimeOfRide, startLocation, endLocation, numberOfPeople, willingToPay, payment):
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


#view_available_postings (note: to add restriction to viewing postings targeted towards the requesting user type)
@api_view(['GET'])
def get_available_postings(request, category):
    query_set = ''
    if category == '':
        query_set = Posting.objects.all()
    else:
        query_set = Posting.objects.filter(category=category)
	
    serializer = PostingSerializer(query_set, many=True)
    json = JSONRenderer().render(serializer.data)

    #return Response(json)
    return Response(serializer.data)

@api_view(['GET'])
def get_postings_by_id(request, user_id_num):
    print("user_id_num: ")
    print(user_id_num)
    #query_set = Posting.objects.all()
    #query_set = Posting.objects.filter(category=user_id_num)
    query_set = Posting.objects.filter(user=user_id_num)
	
    serializer = PostingSerializer(query_set, many=True)
    json = JSONRenderer().render(serializer.data)

    #return Response(json)
    return Response(serializer.data)
    
    
def edit_rideposting(request, key, startLocation):
    rideposting = RidePosting.objects.get(pk=key)
    rideposting.startLocation = startLocation
    rideposting.save()
    return render(request, 'sample/posting_list.html')

    
def delete_rideposting(request, key):
    rideposting = RidePosting.objects.get(pk=key)
    rideposting.delete()
    return render(request, 'sample/posting_list.html')


def editItemPosting(request, item_pk, posting_pk, images, price, forSale, forLoan):
    post = ItemPosting.objects.get(pk=item_pk)
    # use is_valid?
    post.images = images
    post.price = price
    post.forSale = forSale
    post.forLoan = forLoan
    post.save()
    serializer = ItemPostingSerializer(post)
    return Response(serializer.data)  # not sure if this is best way to do thsi


def deleteItemPosting(request, item_pk):
    post = ItemPosting.objects.get(pk=item_pk)
    post.delete()
    return render(request, 'sample/posting_list.html')  # replace HTML File


# SEARCH FUNCTION
def searchPostings(request, keyword):
    postingList = Posting.objects.filter(description__contains=keyword)  # is this the filter we want?
    serializer = PostingSerializer(postingList, context={'request': request}, many=True)
    return Response(serializer.data)


# MARK POSTING SOLD
def postingFulfilledToggle(request, pk):
    post = Posting.objects.get(pk=pk)
    if post.fulfilled:
        post.fulfilled = False
    else:
        post.fulfilled = True
    post.save()
    return render(request, 'sample/posting_list.html')  # replace HTML File


# VIEW DETAILS - JUST RETURN ALL THE INTEL?
# do we need one of these for item/ride as well?
def viewDetails(request, pk):
    post = Posting.objects.get(pk=pk)
    serializer = PostingSerializer(post, context={'request': request}, many=True)
    return Response(serializer.data)



# #USERS
# @api_view(['POST'])
# def create_user(request, name, email, role):
