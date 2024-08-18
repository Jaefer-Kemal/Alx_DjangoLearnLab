from django.urls import path
#1st
from .views import list_books, LibraryDetailView
#2nd
from .views import LoginView, LogoutView
from . import views
from .views import admin_view, librarian_view, member_view, register
#3rd
from django.urls import path
from .views import add_book, edit_book, delete_book


urlpatterns = [
    # Existing URL patterns
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    # Secured views for books
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]
