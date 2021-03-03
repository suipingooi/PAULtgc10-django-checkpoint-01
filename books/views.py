from django.shortcuts import render
from .models import Book

# Create your views here.


# define a view function
def index(request):
    books = Book.objects.all()  # eqv. SELECT * FROM books
    return render(request, "books/index-template.html", {
        'books': books
    })
