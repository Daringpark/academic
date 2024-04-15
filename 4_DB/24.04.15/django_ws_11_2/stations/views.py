from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Station, Location
from .serializers import StationSerializer, StatitionListSerializer, LocationSerializer


# Create your views here.

@api_view(['POST'])
def location(request):
    location = LocationSerializer(data = request.data)
    if location.is_valid(raise_exception=True):
        location.save()
        return Response(location.data, status = status.HTTP_201_CREATED)

@api_view(['POST'])
def station_create(request, location_pk):
    location = Location.objects.get(pk = location_pk)
    serializer = StationSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(address = location)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

# 전체 stations 목록 조회
@api_view(['GET'])
def station(request):
    stations = Station.objects.all()
    serializer = StatitionListSerializer(stations, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

# station 상세
@api_view(['GET'])
def station_detail(request, station_pk):
    station = Station.objects.get(pk = station_pk)
    serializer = StationSerializer(station)
    return Response(serializer.data, status = status.HTTP_200_OK)
