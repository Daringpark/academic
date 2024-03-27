from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm

# Create your views here.
def index(request):
    memo = Memo.objects.all()
    context = {
        'memos' : memo
    }
    return render(request, 'memos/index.html', context)

def create(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memos:index')
    else:
        form = MemoForm()
    context = {
        'form' : form,
    }
    return render(request, 'memos/create.html', context)

def detail(request, pk):
    # memo = Memo.objects.get(pk = pk)
    memo = get_object_or_404(Memo, pk = pk)
    context = {
        'memo' : memo
    }
    return render(request, 'memos/detail.html', context)

def edit(request, pk):
    memo = Memo.objects.get(pk = pk)
        
    if request.method == "POST":
        form = MemoForm(request.POST, instance = memo)
        if form.is_valid():
            form.save()
            return redirect('memos:detail', memo.pk)
        
    else:
        form = MemoForm(instance = memo)
        
    context = {
        'form' : form,
        'memo' : memo,
    }
    
    return render(request, 'memos/edit.html', context)

def delete(request, pk):
    memo = Memo.objects.get(pk = pk)
    memo.delete()
    return redirect('memos:index')