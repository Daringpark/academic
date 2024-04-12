from django.urls import path
from . import views

app_name = 'trends'
urlpatterns = [
    path('keyword/', views.keyword, name = 'keyword'),
    path('keyword/<int:key_pk>/', views.kw_delete, name = 'kw_delete'),
    path('crawling/', views.crawling, name = 'crawling'),
    path('crawling/histogram/', views.histo, name = 'histo'),
    path('crawling/advanced/', views.advanced, name = 'advanced'),
]
