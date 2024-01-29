import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])
# print(parsed_data['company']['name'])

dummy_data = []
# parsed_data[i]['address']['geo']['lat']

for i in range(len(parsed_data)) :
    
    if -80 < (float(parsed_data[i]['address']['geo']['lat']) 
            and float(parsed_data[i]['address']['geo']['lng'])) < 80 :
        dic = {}
        dic['company'] = parsed_data[i]['company']['name']
        dic['lat'] = parsed_data[i]['address']['geo']['lat']
        dic['lng'] = parsed_data[i]['address']['geo']['lng']
        dic['name'] = parsed_data[i]['name']

        dummy_data.append(dic)

print(dummy_data)
