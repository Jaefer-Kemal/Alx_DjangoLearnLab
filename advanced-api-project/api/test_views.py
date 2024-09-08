from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test author and book instance for CRUD operations
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year="2023",  
            author=self.author
        )
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        # Test creating a new book
        data = {
            'title': 'New Book',
            'publication_year': '2024',
            'author': self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        # Test updating an existing book's title
        data = {'title': 'Updated Book Title'}
        response = self.client.patch(self.book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        # Test filtering books by title
        response = self.client.get(self.book_list_url, {'title': 'Test Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Adjusted to handle non-paginated response

    def test_search_books(self):
        # Test searching books by title
        response = self.client.get(self.book_list_url, {'search': 'Test Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_books(self):
        # Test ordering books by title
        response = self.client.get(self.book_list_url, {'ordering': 'title'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Simple check to see if titles are ordered
        books = [book['title'] for book in response.data]
        self.assertEqual(books, sorted(books))
