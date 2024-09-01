from django.shortcuts import render
import rest_framework
import rest_framework.generics
from .serializers import BookSerializer
from .models import Book

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
