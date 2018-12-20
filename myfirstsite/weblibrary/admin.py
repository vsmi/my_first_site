from django.contrib import admin
from .models import Book, BookList

# Register your models here.
admin.site.register(Book)
admin.site.register(BookList)