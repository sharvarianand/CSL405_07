from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from django.http import JsonResponse
from datetime import date

# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def home_view(request):
    # Check if Accept header includes text/html
    if 'text/html' in request.META.get('HTTP_ACCEPT', ''):
        # Return HTML template for browsers
        today = date.today().strftime("%B %d, %Y")
        return render(request, 'library_app/home.html', {'today': today})
    else:
        # Return JSON for API clients
        return JsonResponse({
            "message": "Welcome to the Library Management API",
            "date": date.today().strftime("%Y-%m-%d"),
            "endpoints": {
                "authors_list": "/api/authors/",
                "authors_detail": "/api/authors/{id}/",
                "books_list": "/api/books/",
                "books_detail": "/api/books/{id}/"
            }
        })