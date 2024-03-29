from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('profile', views.about),
    path('skills', views.skill),
    path('project', views.project),
    path('contact', views.contact),
]
