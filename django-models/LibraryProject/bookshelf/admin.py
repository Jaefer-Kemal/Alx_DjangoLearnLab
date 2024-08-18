from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Use 'published_date' instead of 'publication_year'
    list_filter = ('author', 'published_date')  # Use 'published_date' instead of 'publication_year'
    search_fields = ('title', 'author')
