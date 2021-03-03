from django.shortcuts import render, HttpResponse

# Create your views here.


# define a view function
def index(request):
    return HttpResponse("Hello World")
