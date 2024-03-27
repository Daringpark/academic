from django import forms
from .models import Reservation

# Create your models here.
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
