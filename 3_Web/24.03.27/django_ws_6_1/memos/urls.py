from . import views
from django.urls import path

app_name = 'memos'
urlpatterns = [
    path('', views.index, name = 'index'),
    # CRUD
    path('create/', views.create, name = 'create'),
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/delete', views.delete, name = 'delete'),
]
