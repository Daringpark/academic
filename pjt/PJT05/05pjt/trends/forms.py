from .models import Keyword, Trend
from django import forms

# Create your models here.
class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ("name", )
        labels = {
            "name" : '키워드'
        }