from relationship_app.models import Author, Book, Library, Librarian

library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

library_name = "Central Library"
library = Library.objects.get(name=library_name)
Librarian.objects.get(library="")