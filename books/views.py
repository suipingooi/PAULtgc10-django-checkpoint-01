from django.shortcuts import render

# Create your views here.


# define a view function
def index(request):
    return render(request, "books/index-template.html")
