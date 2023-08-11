
#!Django modules and functions
from django.urls import path

from .views import ListBooks

app_name = 'book'
urlpatterns = [
    path('get/books/',ListBooks.as_view(),name='get-books')
]
