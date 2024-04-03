from django import forms
from .models import Restaurant

# Create your forms here.
class RestCreationForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = "__all__"