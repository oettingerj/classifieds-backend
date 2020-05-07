from django.conf import settings

from django.contrib.auth.backends import BaseBackend
from auth_app.models import UserManager

from google.oauth2 import id_token
from google.auth.transport import requests

from django.contrib.auth import login

from auth_app.models import User #does this work?

class AuthBackend(BaseBackend):
    def authenticate(self, request):
        print("authenticate method of AuthBackend class in custom_auth module called")
        print("request.data as a dictionary from custom_auth.py: ")
        query_dictionary = request.data
        dictionary = query_dictionary.dict()
        # for key, value in dictionary.items():
        #     print("pair to follow")
        #     print(key, ':', value)
        
        #print(dictionary.get("idtoken"))
        

        try:
            idinfo = id_token.verify_oauth2_token(dictionary.get("idtoken"), requests.Request(), "493676056314-uid03hsi8jvntqufcmivqhg3otrgnkr8.apps.googleusercontent.com")
            print("*****checkpoint 0A*****")
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong token issuer.')
            print("*****checkpoint 0B*****")
            google_account_id = idinfo['sub']
            print("*****checkpoint 0B-1*****")
            print(google_account_id)
            print("*****checkpoint 0B-2*****")
            email = idinfo['email']
            print("email is: " + email)
            given_name = idinfo['given_name']
            last_name = idinfo['family_name']
            role = 'STUDENT' #default to student

            user = None

            print("*****checkpoint 0C*****")
            try:
                print("*****checkpoint 0D*****")
                user = User.objects.get(google_account_id=google_account_id) #settings.AUTH_USER_MODEL.objects.get
                login(request, user,'auth_app.custom_auth.AuthBackend')
                return user
                print("*****checkpoint 0D-1*****")

            except User.DoesNotExist: #settings.AUTH_USER_MODEL.DoesNotExist:
                print("*****checkpoint 0E*****")
                #instanceOfUserManager = UserManager()
                #user = instanceOfUserManager.create_user(google_account_id, email, given_name, last_name, role)
                user = User.objects.create_user(google_account_id, email, given_name, last_name, role)
                login(request, user,'auth_app.custom_auth.AuthBackend')
                return user

            print("*****checkpoint 0F*****")
            #return user

        except ValueError:
            print("*****checkpoint 0G*****")
            print("Authentication error")
            return None
            pass
        print("*****checkpoint 0G*****")
        #login(request, user,'auth_app.custom_auth.AuthBackend')
        print("*****checkpoint 0H*****")
        #return user

    def get_user(self, user_id):
        print()
        print()
        print()
        print()
        print("*****checkpoint 0I*****")
        print(user_id)
        user = User.objects.get(pk=user_id) #settings.AUTH_USER_MODEL.objects.get(pk=user_id)
        print(user)
        print("*****checkpoint 0J*****")
        return user





















# import io
# from rest_framework import status
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response


# class AuthBackendSerialized(BaseBackend):
#     def authenticate(self, request):
#         stream = io.BytesIO(request.body)
#         data = JSONParser().parse(stream)
#         serializer = AuthBackendSerializer(data=data)
       
#         if serializer.is_valid():
#             try:
#                 idinfo = id_token.verify_oauth2_token(request, requests.Request(), "client_id_here")

#                 if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#                     raise ValueError('Wrong token issuer.')

#                 google_account_id = idinfo['sub']
#                 email = idinfo['email']
#                 given_name = idinfo['given_name']
#                 last_name = idinfo['family_name']
#                 role = 'STUDENT' #default to student

                
#                 try:
#                     user = User.objects.get(username=google_account_id)

#                 except User.DoesNotExist:
#                     user = UserManager.create_user(google_account_id, email, given_name, last_name, role)

#                 return user

#             except ValueError:
#                 print("Authentication error")
#                 pass
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)