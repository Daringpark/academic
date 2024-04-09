from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('accounts:profile', author.user.username)
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'libraries/create_author.html', context)

def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/books.html', context)

def books_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:books')
    else:
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'libraries/books_create.html', context)

def author_books(request, author_pk):
    author = Author.objects.get(pk = author_pk)
    books = Book.objects.all().filter(author = author)
    context = {
        'author' : author,
        'books' : books
    }
    return render(request, 'libraries/author_books.html', context)

@login_required
def subscirbe(request, author_pk):
    author = Author.objects.get(pk = author_pk)
    if request.user in author.subscribed_users.all():
        author.subscribed_users.remove(request.user)
    else:
        author.subscribed_users.add(request.user)

    return redirect('libraries:author_books', author_pk)

# 어떤걸 기준으로 잡을지가 중요하다.
# user를 기준으로 잡을거면 어느 테이블에서 가져올 것인가? 애초에 요청한 user의 값을 가져올 것이다.
# request.user."related_name".add or remove

# 그럼, author를 기준으로 하려면?
# Author model 안에 행으로 존재하는 ManyToManyField가 있기 때문에 author."col_name".add or remove