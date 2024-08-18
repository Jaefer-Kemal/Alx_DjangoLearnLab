from relationship_app.models import Author, Book, Library, Librarian

library = Library.objects.get(name="Central Library")
books_by_author = Book.objects.filter(author__name="author_name")
librarian_for_library = Librarian.objects.get(library__name='library_name')
