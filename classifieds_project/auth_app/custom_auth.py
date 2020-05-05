from django.conf import settings

from django.contrib.auth.backends import BaseBackend
from auth_app.models import UserManager

from google.oauth2 import id_token
from google.auth.transport import requests

class AuthBackend(BaseBackend):
    def authenticate(self, request):
        print("authenticate method of AuthBackend class in custom_auth module called")
        print("request.data as a dictionary from custom_auth.py: ")
        query_dictionary = request.data
        dictionary = query_dictionary.dict()
        for key, value in dictionary.items():
            print("pair to follow")
            print(key, ':', value)
        

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
                user = settings.AUTH_USER_MODEL.objects.get(username=google_account_id)

            except settings.AUTH_USER_MODEL.DoesNotExist:
                user = UserManager.create_user(google_account_id, email, given_name, last_name, role)

            return user

        except ValueError:
            print("Authentication error")
            pass

    def get_user(user_id):
        user = settings.AUTH_USER_MODEL.objects.get(pk=user_id)
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