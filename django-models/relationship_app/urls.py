from django.urls import path
#1st
from .views import list_books, LibraryDetailView
#2nd
from .views import LoginView, LogoutView
from . import views
from .views import admin_view, librarian_view, member_view, RegisterView
#3rd
from django.urls import path
from .views import add_book, edit_book, delete_book


urlpatterns = [
    # Existing URL patterns
     path('', list_books, name='book_list'),  # Adjust the path if needed
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
