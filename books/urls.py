from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib import admin
from .views import book_list

urlpatterns = [
    path('list/', book_list, name='book_list'),
]