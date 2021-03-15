from django.contrib import admin

# Register your models here.
from .models import Book, Publisher, Genre, Tag

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Tag)
