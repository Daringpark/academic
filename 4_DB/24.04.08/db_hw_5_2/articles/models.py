# articles/models.py
from django.db import models
from accounts.models import User

class Article(models.Model):

    # users = models.ManyToManyField(User, through = 'Article_like_users')
    # N:M 중개모델을 지정 "through"
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # article_
    like_users = models.ManyToManyField(User, related_name="like_articles")
    # like_articles라는 이름으로
    title = models.CharField(max_length = 10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# 중개모델 사용시
# class Article_like_users(models.Model):
    
    # article = models.ForeignKey(Article, on_delete = models.CASCADE)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)