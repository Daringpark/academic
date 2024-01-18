
# # 사용자 정의 모듈 불러오기
# import my_func

# my_func.add(3,4)

# # PSL (Python Standard Library)

# import pandas # pandas library 사용

# # 사용자 정의 패키지 사용하기

# from my_pack.math import my_func
# from my_pack.tools import mod

# my_func.add(7, 5) # add() = x + y
# mod.mod(12, 2) # mod() = x//y

# 외부 패키지를 불러오기

import requests

url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()

print(response)
