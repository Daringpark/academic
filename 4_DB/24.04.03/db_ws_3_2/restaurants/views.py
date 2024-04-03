from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestCreationForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'restaurants/index.html', context)

def create(request):
    if request.method == 'POST':
        RestaurantCreatationForm = RestCreationForm(request.POST)
        if RestaurantCreatationForm.is_valid():
            RestaurantCreatationForm.save()
            return redirect('restaurants:index')
    RestaurantCreatationForm = RestCreationForm()
    context = {
        'restaurantForm' : RestaurantCreatationForm
    }
    return render(request, 'restaurants/create.html', context)


def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk = restaurant_pk)
    context = {
        'restaurant' : restaurant
    }
    return render(request, 'restaurants/detail.html', context)