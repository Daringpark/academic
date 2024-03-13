import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'Jane',
        'age' : 24,
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    picked = random.choice(foods)
    foods.pop(foods.index(picked))
    context = {
        'foods' : foods,
        'picked' : picked
    }
    
    return render(request, 'articles/dinner.html', context)

def base(request):
    return render(request, 'articles/base.html')

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('throw_1')
    # input에서 받아오는 request message를 value화
    context = {
        'throw' : message,
    }
    
    return render(request, 'articles/catch.html', context)
