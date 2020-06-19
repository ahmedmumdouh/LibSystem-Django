from .models import Book
from rest_framework import serializers


class BookApi(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'


