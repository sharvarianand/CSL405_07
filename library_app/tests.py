from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Author, Book
from datetime import date

today = date.today()

class AuthorModelTests(TestCase):
    def test_author_creation(self):
        author = Author.objects.create(name='Test Author')
        self.assertEqual(author.name, 'Test Author')

class BookModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        
    def test_book_creation(self):
        book = Book.objects.create(
            title='Test Book',
            isbn='1234567890123',
            author=self.author
        )
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, self.author)

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            isbn='1234567890123',
            author=self.author
        )
        
    def test_get_authors(self):
        response = self.client.get(reverse('author-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_books(self):
        response = self.client.get(reverse('book-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
