from django.urls import path
from . import views

urlpatterns = [
    path('libraries/', views.book_list, name = "book_list"),
    path('libraries/<int:book_pk>/', views.book_detail, name = "book_detail"),
]
