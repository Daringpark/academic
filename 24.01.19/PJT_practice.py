
# 서버에서 데이터를 가져와 보세요.

import requests
from pprint import pprint as print



# request library의 get(), json()
API_key = '2b4dc0583ce79e94e103197c0386d245'
lat = 35.14
lon = 129.06
# 부산으로 떠나보자

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
data = requests.get(url).json()
print(data)

# print(data['weather'][0]['description'])

# data['weather']
# data.get('weather')
