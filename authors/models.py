from django.db import models
from books_cbv.models import Book

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def getBooks(self):
        return Book.objects.filter(author_id=self.id)
