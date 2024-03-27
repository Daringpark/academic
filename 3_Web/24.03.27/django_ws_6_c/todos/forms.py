from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['is_completed']
        is_completed = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
        
        # is_completed = forms.BooleanField(
        #     widget= forms.HiddenInput(
        #         attrs={
                    
        #         }
        #     )
        # )