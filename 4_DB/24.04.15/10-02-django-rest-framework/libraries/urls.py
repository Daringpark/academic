from django.urls import path
from . import views

urlpatterns = [
    path('libraries/', views.book_list),
    path('libraries/<int:book_pk>/', views.book_detail),
    path('libraries/<int:book_pk>/reviews/', views.create_review),
    path('reviews/', views.reviews),
]
