from django.db import models
from accounts.models import User

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) # 작성자 정보
    title = models.CharField(max_length = 20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    parent = models.ForeignKey('self', blank = True, null = True, related_name = 'comment_parent', on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()


class movie_like_users(models.Model):
    # 좋아요 누른 유저 정보
    # 1:N, 1:N
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE) 
    user = models.ForeignKey(User, on_delete = models.CASCADE)