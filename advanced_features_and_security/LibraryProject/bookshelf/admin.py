from django.contrib import admin
from .models import Book,  CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Corrected field name
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author')
    
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
