from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address')
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)

class CustomUserUpdateFrom(UserChangeForm):
    email = forms.EmailField(label = 'Email address')

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', )