from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    # define a VARCHAR using Django
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)

    # TextField is the TEXT in MySQL (65000 characters)
    desc = models.TextField(blank=False)

    # define the relationship with the genre
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    # define the relationship with the tags
    tags = models.ManyToManyField('Tag')

    # define the relationship with the publisher model
    # models.CASCADE means -- if the publisher is deleted, then
    # the book will be deleted as well
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    # define the M:N relationship with authors
    authors = models.ManyToManyField('Author')

    # store user
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False, max_length=320)

    # toString function
    def __str__(self):
        return self.name + " (" + self.email + ")"


class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    date_of_birth = models.DateTimeField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
