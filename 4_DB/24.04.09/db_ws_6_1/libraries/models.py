from django.db import models
from accounts.models import User

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    subscribed_users = models.ManyToManyField(User , related_name="subcriber")
    nickname = models.CharField(max_length = 20)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.TextField()