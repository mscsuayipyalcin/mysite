from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import  Books
# Create your views here.

def book_list(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'kitaplar':books,})