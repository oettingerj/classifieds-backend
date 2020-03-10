# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
  
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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


# @api_view(['GET', 'POST'])
@api_view(['POST'])
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
    serializer = PostingSerializer(data=temp_dictionary)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','POST'])
def import_itemposting(request, posting_pk, images, price, forSale, forLoan):
    temp_dictionary = {
        'posting': posting_pk,
        #'images': images, #intentionally excluded for importing test data
        'price': price,
        'forSale': forSale,
        'forLoan': forLoan
    }
    serializer = ItemPostingSerializer(data=temp_dictionary)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def import_rideposting(request, posting_pk, dateTimeOfRide, startLocation, endLocation, numberOfPeople):
    temp_dictionary = {
        'posting': posting_pk,
        'dateTimeOfRide': dateTimeOfRide,
        'startLocation': startLocation,
        'endLocation': endLocation,
        'numberOfPeople': numberOfPeople
        }

    serializer = RidePostingSerializer(data=temp_dictionary)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
''' example of retriving postings'''
def posting_list(request):
    postings = Posting.objects.filter(category='Toys')
    return render(request, 'sample/posting_list.html', {'postings': postings})
