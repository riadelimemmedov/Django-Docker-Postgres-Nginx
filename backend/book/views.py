from django.shortcuts import render
from rest_framework.views import APIView,status
from rest_framework.response import Response
from rest_framework.request import Request


from .models import Book
from .serializers import BookSerializer

# Create your views here.


#*ListBooks
class ListBooks(APIView):
    lookup_field="book_author"
    
    def get(self,request,format=None):
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books,many=True,context={"request":request})
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'error':'Dont have exists any book object in database'},status=status.HTTP_404_NOT_FOUND)