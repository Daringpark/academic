
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

# # 외부 패키지를 불러오기

# import requests

# url = 'https://random-data-api.com/api/v2/users'
# response = requests.get(url).json()

# print(response)

# for문 연습

for i in str('간장공장공장장') : # string도 iterable함을 알자.
    print('+_+', end = ' ')
    print(f'<<({i})')

my_dict = {'이름' : '홍길동', '나이' : 32, '성별' : '남'}

for key in my_dict :
    print(f'==={key}===')
    print(my_dict[key])

my_list = [1,2,3,4,5,6,7,8,9,10]
n = len(my_list)

print(my_list)
for i in range(n) :
    my_list[i] = my_list[i] + 10
    print(my_list[i])
print(my_list)

outers = ['A', 'B', 'C']
inners = [1,2,3,4,5]

for i in outers :
    for j in inners:
        print(i, j)
        if j == 5 :
            print('----')

n = int(input('양의 정수를 입력하세요 : '))

while n <= 0 :
    if n < 0 :
        print('- 음수를 기입했습니다. 다시 입력하세요.')
    else :
        print('- 0을 입력했습니다. 다시 입력해주세요.')
    n = int(input('양의 정수를 입력하세요 : '))

print(f'- 양의 정수를 입력했습니다.\n{n}는 양의 정수입니다.')

# False가 될 때까지라고 이해하면 좋다.




