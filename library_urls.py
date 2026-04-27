from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('author/add/', views.add_author, name='add_author'),
    path('authors/', views.author_list, name='author_list'),
    path('author/<int:author_id>/', views.author_books, name='author_books'),
    path('api/books/', views.BookListCreateView.as_view(), name='book_list_create'),
    path('api/books/<int:pk>/', views.BookRetrieveUpdateView.as_view(), name='book_detail'),
]