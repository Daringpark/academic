from django.db import models
from todo_list_project import settings

# Create your models here.
class Diary(models.Model):
    content = models.CharField(max_length=125)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "likes_diary")
    picture = models.ImageField(blank=True, upload_to='diary/%y/%b/%a')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)