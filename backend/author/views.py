from django.shortcuts import render
from rest_framework.views import APIView,status
from rest_framework.response import Response
from rest_framework.request import Request


from .models import Author
from .serializers import AuthorSerializer

# Create your views here.


#*ListAuthors
class ListAuthors(APIView):
    def get(self,request,format=None):
        try:
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Author.DoesNotExist:
            return Response({'error':'Dont have exists any author object in database'},status=status.HTTP_404_NOT_FOUND)