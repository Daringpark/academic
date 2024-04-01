from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    
     class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        # 모델은 지금 사용하고 있는 모델을 사용하면서
        model = get_user_model()

        # 필드 정의를 해줘야합니다.
        fields = ('first_name', 'last_name', )