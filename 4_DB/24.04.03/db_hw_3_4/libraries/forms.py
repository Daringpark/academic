from .models import Book
from django import forms


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'adult', 'price', )
