from django.shortcuts import render, redirect
from .models import Book
from .forms import AuthorForm, BookCreationForm

# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

def books(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'libraries/books.html', context)

def create(request):
    if request.method == "POST":
        form = BookCreationForm(request.POST, request)
        if form.is_valid():
            book = form.save(commit = False)
            book.save()
        return redirect('libraries:books')

    form = BookCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'libraries/create.html', context)

def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request)
        if form.is_valid():
            author = form.save(commit = False)
            author.user_id = request.user.pk
            author.save()
        return redirect('accounts:profile', request.user.username)

    form = AuthorForm()
    context = {
        'form' : form,
    }
    return render(request, 'libraries/create_author.html', context)