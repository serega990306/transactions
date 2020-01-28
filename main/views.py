from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer, AuthSerializer
from .models import Account
from django.shortcuts import get_object_or_404


@api_view(['POST',])
def registration_view(request):

    serializer = RegistrationSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "Successful registration!"
    else:
        data['response'] = "Registration error!"

    return Response(data)


@api_view(['POST',])
def auth_view(request):

    serializer = AuthSerializer(data=request.data)
    data = {}

    user = get_object_or_404(Account, email=request.POST.get('email', ''), password=request.POST.get('password', ''))

    if user:
        data['response'] = "Success!"
    else:
        data['response'] = "Error!"

    return Response(data)
