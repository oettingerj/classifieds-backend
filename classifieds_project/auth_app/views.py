from auth_app.custom_auth import AuthBackend

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def authenticate(request):
    print("authenticate method in views module called")

    print("request.data from views.py: ") 
    print(request.data)

    instance_of_AuthBackend_class = AuthBackend()
    instance_of_AuthBackend_class.authenticate(request)
    return Response("success from views.py of auth_app")