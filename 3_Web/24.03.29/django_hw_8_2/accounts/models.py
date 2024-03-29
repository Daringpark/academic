from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    AUTH_USER_MODEL = 'accounts.User'