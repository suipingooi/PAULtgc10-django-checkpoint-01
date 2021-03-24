from django.shortcuts import render, redirect, reverse
from .forms import ReviewForm
from django.contrib import messages
from .models import Review

# Create your views here.


def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index-template.html', {
        'reviews': reviews
    })


def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ownder = request.user
            review.save()
            messages.success(request, 'New review has been added')
            return redirect(reverse(show_reviews))

    else:
        create_form = ReviewForm()

        return render(request, 'reviews/create-template.html', {
            'form': create_form
        })
