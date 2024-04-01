from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 django project에서 활성화된 User 객체를 반환하는 함수
        model = get_user_model()
