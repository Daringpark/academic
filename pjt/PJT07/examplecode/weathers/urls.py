from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('temp/', views.temp, name = 'tempbydt'),
    path('hottemp/', views.hot_weathers, name = 'hottemp'),
]
