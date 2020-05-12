from auth_app.custom_auth import AuthBackend
from django.contrib.auth import logout as logout_user
from django.middleware import csrf

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def authenticate(request):
    instance_of_AuthBackend_class = AuthBackend()
    user = instance_of_AuthBackend_class.authenticate(request)
    csrf_token = csrf.get_token(request)
    if user is not None:
        data = {
            'name': f'{user.given_name} {user.last_name}',
            'email': user.email,
            'id': user.id,
            'csrfToken': csrf_token
        }
        response = Response(data=data, status=status.HTTP_200_OK)

        return response
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'POST'])
def logout(request):
    logout_user(request)

    return Response(status=status.HTTP_200_OK)
