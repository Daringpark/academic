from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # submit했던 데이터 불러오기
    title = request.POST.get('title')
    content = request.POST.get('content')
    # django-extensions
    article = Article(title = title, content = content)
    article.save()
    return redirect('articles:index')

def delete(request, pk):
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 조회하기
    article = Article.objects.get(pk = pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 수정해주기
    article.title = title
    article.content = content
    article.save()
    
    return redirect('articles:detail', article.pk)