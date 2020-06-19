from .models import Author
from rest_framework import serializers
from django.contrib.auth.models import User

class AuthorApi(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'


class UserApi(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        