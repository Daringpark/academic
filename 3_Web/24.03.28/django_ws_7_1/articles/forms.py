from django import forms
from .models import Article

# Create your models here.
class ContentForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"