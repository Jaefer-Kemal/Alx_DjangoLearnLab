from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        pass
    
    return render(request, 'create_book.html')

def book_list(request):
    books = Book.objects.all() 
    return render(request, 'book_list.html', {'books': books})