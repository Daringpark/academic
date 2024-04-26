from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
import requests
from django.conf import settings

# Create your views here.
# API_URL로 데이터 요청하기
def index(request):
    city_name = 'Seoul,KR'
    api_key = settings.WEATHER_API_KEY

    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()

    # print(response)
    return JsonResponse(response)

# API_URL로 요청 이후, 데이터 불러와 저장하기 
from .serializers import WeatherSerializer
def temp(request):
    city_name = 'Seoul,KR'
    api_key = settings.WEATHER_API_KEY

    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    
    for li in response.get('list'):
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')

        print(dt_txt)

        li_data = {
            'dx_txt' : dt_txt,
            'temp' : temp,
            'feels_like' : feels_like,
        }

        weatherserializer = WeatherSerializer(data = li_data)
        if weatherserializer.is_valid(raise_exception = True):
            weatherserializer.save()

    return JsonResponse({"message" : "all save!!"})


# 저장된 DB에서 불러오기
from rest_framework.decorators import api_view
from .models import Weather
@api_view(['GET'])
def hot_weathers(request):

    weathers = Weather.objects.all()
    hot_weather_list = []

    for weather in weathers:
        celsius = round(weather.temp - 273.15, 2)
        if celsius >= 20:
            hot_weather_list.append(weather)

    serializer = WeatherSerializer(hot_weather_list, many = True)
    return Response(serializer.data)