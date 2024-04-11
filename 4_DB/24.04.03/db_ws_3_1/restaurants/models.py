from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20)

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_vegan = models.BooleanField()

    def __str__(self):
        return self.name