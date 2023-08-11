
#!Django modules and functions
from django.urls import path

from .views import ListAuthors

app_name = 'author'
urlpatterns = [
    path('get/authors/',ListAuthors.as_view(),name='get-authors')
]
