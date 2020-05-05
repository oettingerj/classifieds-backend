
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser
)
from django.db import models
from datetime import datetime
# from .serializers import (
#     UserSerializer, 
#     AuthBackendSerializer, 
#     PostingSerializer, 
#     ItemPostingSerializer, 
#     RidePostingSerializer
# )
import io
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth.backends import BaseBackend

# from google.oauth2 import id_token
# from google.auth.transport import requests

class UserManager(BaseUserManager):
    def create_user(self, google_account_id, email, given_name, last_name, role):
        new_user = self.model (
            google_account_id = google_account_id,
            email = email,
            given_name = given_name,
            last_name = last_name,
            role = role,
        )

        new_user.set_unusable_password()
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, google_account_id, email, given_name, last_name, role, password=None):
        new_superuser = self.model (
            google_account_id = google_account_id,
            email = email,
            given_name = given_name,
            last_name = last_name,
            is_superuser = True,
            role = role,
        )

        new_superuser.set_password(password)
        new_superuser.save(using=self._db)
        return new_superuser

class User(AbstractBaseUser):
    #password field inhereted from AbstractBaseUser
    USERNAME_FIELD = 'google_account_id'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    google_account_id = models.TextField(default="no id")
    email = models.EmailField(unique=True)
    given_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=150)
    date_joined = models.DateTimeField(default=datetime.now)
    last_login = models.DateTimeField(default=datetime.now)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    roleChoice = models.TextChoices('roleChoice', 'STUDENT FACULTY STAFF ALL')
    role = models.CharField(choices=roleChoice.choices, max_length=7)

    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()

    
    def __str__(self):
        description = "Google ID: " + self.google_account_id + " " + "Last name: " + self.last_name
        return description


    
class AuthBackend(BaseBackend):
    def authenticate(self, request):
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = AuthBackendSerializer(data=data)
       
        if serializer.is_valid():
            try:
                idinfo = id_token.verify_oauth2_token(request, requests.Request(), "client_id_here")

                if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                    raise ValueError('Wrong token issuer.')

                google_account_id = idinfo['sub']
                email = idinfo['email']
                given_name = idinfo['given_name']
                last_name = idinfo['family_name']
                role = 'STUDENT' #default to student

                
                try:
                    user = User.objects.get(username=google_account_id)

                except User.DoesNotExist:
                    user = UserManager.create_user(google_account_id, email, given_name, last_name, role)

                return user

            except ValueError:
                print("Authentication error")
                pass
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeprecatedUser(models.Model):
    username = models.CharField(max_length=240)
    password = models.CharField(max_length=240)
    

    email = models.EmailField(unique=True)
    roleChoice = models.TextChoices('roleChoice', 'STUDENT FACULTY STAFF ALL')
    role = models.CharField(choices=roleChoice.choices, max_length=7)
    dummy_field = models.CharField(max_length=240, default='dummy')


    def __str__(self):
        return self.name


class Posting(models.Model):
    user = models.ForeignKey(User, related_name='poster', on_delete=models.CASCADE)
    timePosted = models.DateTimeField()
    category = models.CharField(max_length=240)  # change to choices later
    prospective = models.BooleanField()
    fulfilled = models.BooleanField()
    title = models.TextField(default="N/A")
    description = models.TextField()
    audienceChoice = models.TextChoices('audienceChoice', 'STUDENT FACULTY STAFF ALL')
    audience = models.CharField(choices=audienceChoice.choices, max_length=7)
    savedBy = models.ManyToManyField(User, related_name='savedPostings')
#title?

class RidePosting(models.Model):
    posting = models.OneToOneField(Posting, on_delete=models.CASCADE)
    dateTimeOfRide = models.DateTimeField()
    startLocation = models.TextField()
    endLocation = models.TextField()
    numberOfPeople = models.IntegerField()
    willingToPay = models.BooleanField()
    payment = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')


class ItemPosting(models.Model):
    posting = models.OneToOneField(Posting, on_delete=models.CASCADE)
    images = models.ImageField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    forSale = models.BooleanField()
    forLoan = models.BooleanField()



