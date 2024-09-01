from django.shortcuts import render
import rest_framework
import rest_framework.generics
import rest_framework.viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    
class BookViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
