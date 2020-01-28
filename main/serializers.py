from rest_framework import serializers
from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['balance', 'currency', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'password']
