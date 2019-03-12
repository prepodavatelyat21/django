from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
  path('', views.AuthorList.as_view(), name='author_list'),
  path('new', views.AuthorCreate.as_view(), name='author_new'),
  path('edit/<int:pk>', views.AuthorUpdate.as_view(), name='author_edit'),
  path('delete/<int:pk>', views.AuthorDelete.as_view(), name='author_delete'),
    ]