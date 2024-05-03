from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('guess/<int:session_pk>/', views.guess, name='guess'),
]
