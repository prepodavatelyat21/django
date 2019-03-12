from django.db import models
from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
    author = models.ForeignKey('authors.Author', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})