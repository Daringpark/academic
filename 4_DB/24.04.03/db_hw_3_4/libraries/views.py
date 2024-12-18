from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import BookCreateForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    creation_form = BookCreateForm()
    books = author.book_set.all()
    context = {
        'author': author,
        'creation_form' : creation_form,
        'books' : books,
    }
    return render(request, 'libraries/detail.html', context)

def book_create(request, author_pk):
    author = Author.objects.get(pk = author_pk)
    creation_form = BookCreateForm(request.POST)
    if creation_form.is_valid():
        book = creation_form.save(commit = False)
        book.author = author
        book.save()
        return redirect('libraries:detail', author_pk)
    
    context = {
        'author' : author,
        'creation_form' : creation_form, 
    }
    return render(request, 'libraries/detail.html', context)
