from rest_framework import serializers
from .models import Author



#!AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        