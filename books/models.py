from django.db import models

# Create your models here.


class Book(models.Model):
    # define a VARCHAR using Django
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)

    # TextField is the TEXT in MySQL (65000 characters)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.title
