from django.contrib import messages
from .forms import BookForm, PublisherForm
from .models import Book, Publisher
from django.shortcuts import render, reverse, redirect, get_object_or_404
# Create your views here.


# define a view function
def index(request):
    books = Book.objects.all()  # eqv. SELECT * FROM books

    # query = Q(genre__exact=2)
    # query = query & Q(tags__in=1, 4)

    # books = books.filter(query)
    # query = ~Q(pk__in=[])

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
            messages.success(
                request, 'New book has been created successfully!')
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


def create_publisher(request):
    if request.method == "POST":
        create_publisher_form = PublisherForm(request.POST)
        if create_publisher_form.is_valid():
            create_publisher_form.save()
            return HttpResponse("New publisher created")
        else:
            return HttpResponse("Error creating publisher")

    else:
        form = PublisherForm()
        return render(request, 'books/create-publisher-template.html', {
            'form': form
        })


def show_publishers(request):
    # select * from publishers
    all_publishers = Publisher.objects.all()
    return render(request, 'books/index-publishers-template.html', {
        'publishers': all_publishers
    })


def update_publisher(request, publisher_id):
    if request.method == "POST":
        # 1. retrieve the publisher object that is being updated
        publisher_being_updated = get_object_or_404(Publisher, pk=publisher_id)

        # 2. create the update form
        update_form = PublisherForm(
            request.POST, instance=publisher_being_updated)

        # 3. check the form for errors
        if update_form.is_valid():
            # if is valid
            update_form.save()
            return redirect(reverse(show_publishers))
        else:
            return render(request, 'books/update-publisher-template.html', {
                'publisher_form': update_form
            })

    else:
        # 1. retrieve the publisher that I want to update from the database
        publisher_to_update = get_object_or_404(Publisher, pk=publisher_id)

        # 2. create the form and initialize its fields with the publisher data
        # from step 1
        publisher_form = PublisherForm(instance=publisher_to_update)

        # 3 rener the form
        return render(request, 'books/update-publisher-template.html', {
            'publisher_form': publisher_form
        })


def delete_publisher(request, publisher_id):
    # process the delete if the method is POST
    if request.method == "POST":
        publisher_to_delete = get_object_or_404(Publisher, pk=publisher_id)
        publisher_to_delete.delete()
        return redirect(reverse(show_publishers))
    else:
        # 1. retrieve the publisher that I want to delete
        publisher_to_delete = get_object_or_404(Publisher, pk=publisher_id)

        return render(request, 'books/delete-publisher-template.html', {
            'publisher': publisher_to_delete
        })
