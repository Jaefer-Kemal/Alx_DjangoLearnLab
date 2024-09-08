from .models import Book, Author  # Importing the Book and Author models from the current module
from rest_framework import serializers  # Importing the serializers module from Django REST Framework (DRF)
from datetime import datetime  # Importing the datetime module to use the current date and time

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    # Meta class to specify the model and fields to include in the serialization
    class Meta:
        model = Book  # The model to be serialized
        fields = "__all__"  # Serializes all fields of the Book model
        
    # Custom validation for the Book model
    def validate(self, data):
        """
        Custom validation method to ensure that the publication year of the book is not in the future.
        If the publication_year is greater than the current year, raise a validation error.
        """
        if data["publication_year"].year > datetime.now().year:  # Check if publication year is in the future
            raise serializers.ValidationError(f"The book publication year should be less than or equal to the current year which is {datetime.now().year}")  # Raise an error with a message
        return data  # Return the validated data if everything is correct
        
# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to include related books in the serialization
    books = BookSerializer(many=True, read_only=True)  # Specifies that the books field is read-only and can have multiple books

    # Meta class to specify the model and fields to include in the serialization
    class Meta:
        model = Author  # The model to be serialized
        fields = "__all__"  # Serializes all fields of the Author model
