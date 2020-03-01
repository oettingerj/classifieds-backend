# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
  
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User, Posting, RidePosting, ItemPosting, Comment
from .serializers import *


@api_view(['GET', 'POST'])
def import_user(request, name, email, role):
    print(str(name))
    print(str(email))
    print(str(role))
    temp_dictionary = {'name': name, 'email': email, 'role': role}

    print("******the data to be passed in is:")
    print(temp_dictionary)
    print("**end of data being passed in**")

    serializer = UserSerializer(data=temp_dictionary)
   

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        print("serializer not valid*********")


    print("this will return a HTTP reponse")

    

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def import_posting(request, user_pk, timePosted, category, prospective, fulfilled, description, audience):
    temp_dictionary = {
        'user': user_pk,
        'timePosted': timePosted,
        'category': category,
        'prospective': prospective,
        'fulfilled': fulfilled,
        'description': description,
        'audience': audience}

    serializer = PostingSerializer(data=temp_dictionary)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        print("serializer not valid*********")


    print("this will return a HTTP reponse")

    

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def import_ridePosting(request, posting_pk, dateTimeOfRide, startLocation, endLocation, numberOfPeople):
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
        print("serializer not valid*********")

    print("this will return a HTTP reponse")

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

