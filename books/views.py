from rest_framework import viewsets, filters
from .serializers import BookSerializer
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    """Listando livros"""
    queryset =Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['author', 'title']
    search_fileds= ['author', 'title' 'id']
    
