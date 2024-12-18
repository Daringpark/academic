from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()