# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
  
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User, Posting, RidePosting, ItemPosting, Comment
from .serializers import *

def import_test(request):
    print("import_test method called")

