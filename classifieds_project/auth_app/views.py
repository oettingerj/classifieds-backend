from auth_app.custom_auth import AuthBackend
from django.contrib.auth import logout as logout_user

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def authenticate(request):
    print("authenticate method in views module called")

    print("request.data from views.py: ") 
    print(request.data)

    instance_of_AuthBackend_class = AuthBackend()
    user = instance_of_AuthBackend_class.authenticate(request)
    if user != None:
        print("*****checkpoint 2A*****")
        request.user = user
        print(request.user)
        return Response(status=status.HTTP_200_OK)
    else:
        print("*****checkpoint 2B*****")
        return Response(status=status.HTTP_403_FORBIDDEN)

    #return Response("success from views.py of auth_app")
    

@api_view(['GET', 'POST'])
def logout(request):
    logout_user(request)

    return Response(status=status.HTTP_200_OK)
