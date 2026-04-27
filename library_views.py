from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import AuthorForm
from rest_framework import generics
from .serializers import BookSerializer


# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()

    return render(request, 'library/add_author.html', {'form': form})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

def author_books(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = author.books.all()

    return render(request, 'library/author_books.html', {
        'author': author,
        'books': books
    })

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
