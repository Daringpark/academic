from django import forms

# Create your models here.
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=12
        # widget= forms.TextInput(
        #     attrs= {'maxlength' : 12,}
        #     )
        )
    password = forms.CharField(widget= forms.PasswordInput())