from django.contrib import admin

from .models import Author, Book, Publisher


class BookToPublisherInline(admin.TabularInline):
    model = Book
    extra = 3


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name', 'age']
    ordering = ['name']


@admin.register(Publisher)
class PublisherModelAdmin(admin.ModelAdmin):
    inlines = [BookToPublisherInline]
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'publisher', 'rating', 'pubdate']
    search_fields = ['name', 'pages', 'price', 'publisher', 'rating', 'pubdate']
    ordering = ['name']
    readonly_fields = ['pubdate']
    sortable_by = ['name', 'price', 'rating', 'pubdate']
