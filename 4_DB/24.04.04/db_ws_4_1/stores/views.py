from django.shortcuts import render, redirect
from .models import Store


# Create your views here.
def index(request):
    stores = Store.objects.all()

    context = {
        'stores' : stores
    }
    return render(request, 'stores/index.html', context)

def store(request, store_pk):
    store = Store.objects.get(pk = store_pk)
    context = {
        'store' : store
    }
    return render(request, 'stores/detail.html', context)