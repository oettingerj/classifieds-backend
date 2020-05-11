from auth_app.custom_auth import AuthBackend
from django.contrib.auth import logout as logout_user

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def authenticate(request):
    instance_of_AuthBackend_class = AuthBackend()
    user = instance_of_AuthBackend_class.authenticate(request)
    if user != None:
        response = Response(status=status.HTTP_200_OK)

        return response
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'POST'])
def logout(request):
    logout_user(request)

    return Response(status=status.HTTP_200_OK)
