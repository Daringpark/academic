from django.urls import path
from . import views

urlpatterns = [
    path('stations/', views.station),
    path('locations/', views.location),
    path('stations/<int:station_pk>/', views.station_detail),
    path('locations/<int:location_pk>/stations/', views.station_create),
]
