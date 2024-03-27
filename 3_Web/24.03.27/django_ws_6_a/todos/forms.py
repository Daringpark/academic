from django import forms
from .models import Todo

# Create your models here.
class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = '__all__'
