from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bookapi import views

urlpatterns = [
    
  path('create',views.BookCreateView.as_view(),name='book_create'),
  path('list',views.BookListView.as_view(),name='book_list'),
  path('update/<int:pk>',views.BookUpdateView.as_view(),name='book_update'),
  path('delete/<int:pk>',views.BookDeleteView.as_view(),name='book_delete'),
  path('detail/<int:pk>',views.BookDetailView.as_view(),name='book_detail'),
  # path('authorcreate',views.AuthorCreateView.as_view(),name='author_create'),
  path('authorupdate/<int:pk>',views.AuthorUpdateView.as_view(),name='author-update'),
  path('authordetails/<int:pk>',views.AuthorDetailView.as_view(),name='author_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)