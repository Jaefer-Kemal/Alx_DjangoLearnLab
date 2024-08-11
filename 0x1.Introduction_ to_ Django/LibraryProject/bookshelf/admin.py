from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    display = ('title', 'author', 'publication_year')
    filter_list = ('author', 'publication_year')
    search = ('title', 'author')
