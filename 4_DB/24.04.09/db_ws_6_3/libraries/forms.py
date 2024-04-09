from django import forms
from .models import Author, Book

# Create your models here.
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('nickname', )

class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
