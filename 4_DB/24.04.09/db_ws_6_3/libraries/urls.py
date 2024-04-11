from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('books/', views.books, name='books'),
    path('books/create/', views.create, name='create'),
    path('create_author/', views.create_author, name='create_author'),

]