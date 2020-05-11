from django.conf import settings

from django.contrib.auth.backends import BaseBackend

from google.oauth2 import id_token
from google.auth.transport import requests

from django.contrib.auth import login

from auth_app.models import User

class AuthBackend(BaseBackend):
    def authenticate(self, request):
        dictionary = request.data

        try:
            idinfo = id_token.verify_oauth2_token(dictionary.get("idtoken"), requests.Request(), "578173933063-2bldsbnkidcvoiq20eqeasv7u6u1fog3.apps.googleusercontent.com")

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong token issuer.')

            google_account_id = idinfo['sub']
            email = idinfo['email']
            given_name = idinfo['given_name']
            last_name = idinfo['family_name']
            role = 'STUDENT' #default to student

            user = None

            try:
                user = User.objects.get(google_account_id=google_account_id)
                login(request, user,'auth_app.custom_auth.AuthBackend')
                
                return user

            except User.DoesNotExist:
                user = User.objects.create_user(google_account_id, email, given_name, last_name, role)
                login(request, user,'auth_app.custom_auth.AuthBackend')
                
                return user

        except ValueError:
            
            return None

    def get_user(self, user_id):
        user = User.objects.get(pk=user_id)

        return user