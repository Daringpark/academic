from django.shortcuts import render, redirect
from .models import Article
from .forms import ContentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ContentForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def detail(request, index_pk):
    article = Article.objects.get(pk=index_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)
    