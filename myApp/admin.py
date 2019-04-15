from django.contrib import admin
from .models import Author, Blog

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'text']