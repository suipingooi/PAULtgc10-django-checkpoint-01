from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
# Create your views here.


# define a view function
def index(request):
    books = Book.objects.all()  # eqv. SELECT * FROM books
    return render(request, "books/index-template.html", {
        'books': books
    })


# for adding a new book
def create_book(request):
    if request.method == 'POST':
        # we want to process the adding of a new book
        create_form = BookForm(request.POST)
        # check if the user has filled in fields correctly
        if create_form.is_valid():
            create_form.save()
            # redirect back to the index function
            return redirect(reverse(index))
        pass
    else:
        create_form = BookForm()  # create an instance of BookForm
        return render(request, 'books/create-template.html', {
            'form': create_form
        })


def update_book(request, book_id):
    if request.method == "POST":
        book_being_changed = get_object_or_404(Book, pk=book_id)
        book_form = BookForm(request.POST, instance=book_being_changed)
        if book_form.is_valid():
            book_form.save()
            return redirect(reverse(index))
    else:
        # 1. retrieve the book that we want to change
        book_being_changed = get_object_or_404(Book, pk=book_id)

        # 2. create the form for the book and populate it with
        #  the existing data
        book_form = BookForm(instance=book_being_changed)

        # 3. display the form
        return render(request, 'books/update-template.html', {
            'form': book_form
        })
