from django.shortcuts import render,redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

def new(request):
    form = ReservationForm()
    context = {
        'form' : form,
    }
    return render(request, 'reservations/new.html', context)
    
def create(request):
    form = ReservationForm(request.POST)
    form.save() # 따로 reservation.pk로 사용할 것 아니면 따로 안가져가도 될 듯
    return redirect('reservations:index') # detail page가 없음