from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author','publication_date')
    list_display_links = ('id', 'title', 'author','publication_date')
    search_fields = ('id', 'title', 'author','publication_date')
    list_per_page = 25
    ordering = ('author',)

admin.site.register(Book, BookAdmin)