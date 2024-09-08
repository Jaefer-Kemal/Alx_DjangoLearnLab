from django.db import models  # Importing the models module from Django


# Defining the Author model
class Author(models.Model):
    # The 'name' field is a character field with a maximum length of 200 characters.
    name = models.CharField(max_length=200)

    # This method defines how to represent an Author instance as a string.
    def __str__(self):
        return f"{self.name}"  # Returns the author's name as the string representation of the object.


# Defining the Book model
class Book(models.Model):
    # The 'title' field is a character field with a maximum length of 200 characters.
    title = models.CharField(max_length=200)

    # The 'publication_year' field is a date field to store the publication date of the book.
    publication_year = models.DateField()

    # The 'author' field is a foreign key that establishes a relationship to the Author model.
    # 'on_delete=models.CASCADE' means that if an author is deleted, all their associated books will also be deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # This method defines how to represent a Book instance as a string.
    def __str__(self) -> str:
        return f"{self.title}"
