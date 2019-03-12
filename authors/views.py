from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from authors.models import Author

class AuthorList(ListView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
    success_url = reverse_lazy('authors:author_list')

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']
    success_url = reverse_lazy('authors:author_list')

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors:author_list')