import math

# k = 550**2 + 600**2
# distance = int(math.sqrt(k))
# print(distance, 'm 입니다.')


# Q. 거스름 돈을 구하는 문제
#시계는 10만원인데, 중고로 팔아서 90%의 가격으로 판매하려고 합니다.
#수중에 만원이 있고, 게임팩은 5만 7천원입니다. 거스름돈은 얼마일까요?

# watch = 100000
# income = watch * 0.9
# gamepack = 57000

# money = 10000 + income
# money = money - gamepack #새로운 개체에 저장하지 않고, money를 갱신해줍니다.

# print('거스름돈은 %d원 입니다.' %money )

# # Q. 파일의 용량을 구하는 문제
# #다운로드하는 파일의 크기를 구해볼까요?
# download_rate = 800
# time = 110

# scale = download_rate * time / 10**3
# print('해당 파일크기는 %dmb 입니다. ' %scale)

# while문 연습
# num = 1
# while num <= 50 :
#     print(num)
#     num += 1

# Q. 입력을 받아 숫자의 크기만큼 반복해서 출력하는 코드를 작성해보세요.
### while을 사용해서 cnt 세기

# cnt = 0
# number = int(input())

# while cnt != number :
#     print(number)
#     cnt += 1

# Q. 정수 한 개를 입력 받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구하는 프로그램을 작성해보자!
### 똑같이 cnt를 세서 해당 수까지 도달하는 전까지 반복하면 되겠죠?

# cnt = 1
# number = int(input())

# while cnt != number + 1 :
#     sq = cnt ** 2
#     print('#%d %d'% (cnt, sq))
#     cnt += 1

# Q. 공을 100미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 높이의 3/5 만큼 뛰어오릅니다.
    # 10번 튀어오를때의 높이를 계산해보세요!

# cnt = 1
# height = 100

# while cnt != 11 :
#     height = round(height * 3/5, 4)
#     print('#%d %fcm' %(cnt, height))
#     cnt += 1

# Q. 30이상은 이해하지 못하는 while문을 만들어볼까요?

# max = 30

# while True :
#     num = int(input())
#     if num >= max : 
#         print('%d가 뭐야?' %num)
#         break
#     else :
#         print('%d는 알아!' %num)

# Q. 입력을 1,2,3 중 하나를 받아 그것을 한글로 출력하는 프로그램을 만들어 볼까요?

# num = int(input())
# numbers = [1,2,3]

# if num in numbers :
#     if num == numbers[-3] :
#         print('일')
#     elif num == numbers[-2] :
#         print('이')
#     elif num == numbers[-1] :
#         print('삼')
# else :
#     print('1,2,3 중 하나를 기입해주세요.')

# Q. 입력을 받아서 세대 구분을 지어봅시다.
    
# print('When were you born in?', '(Input Four digits)')
# year = int(input())

# if year <= 1924 :
#     print('You\'re in The Greatest Generation.' )
# elif year <= 1945 :
#     print('You\'re in The Slient Generation.' )
# elif year <= 1964 :
#     print('You\'re a Baby Bomber.' )
# elif year <= 1980 :
#     print('You\'re in Generation X.' )
# elif year <= 1996 :
#     print('You\'re in Millennial Generation.' )
# else :
#     print('You\'re in Generation Z.' )

# Q. 조건문을 사용하여 단위기호를 넣어봅시다.
    
# num = round(float(input()),3)
# print(num)
# result = str(num)

# if num >= 1000 :
#     result = str(num//1000) + 'k'
# elif num >= 0 :
#     pass

# print('길이는',result+'m입니다.')

# Q. 조건문을 사용하여 양수 입력을 하면 계속 더하다가 음수를 입력하면 중단하고 그전까지의 더한 값을 출력하는 코드를 작성하라.

# sum = 0

# while True :
#     a = int(input())

#     if a >= 0 :
#         sum = sum + a
#     else :
#         break
# print(sum)

# Q. 윤년 계산기를 만들어라.

# year = int(input())
# detect = bool()

# if year % 4 == 0 :
#     if year % 100 == 0 :
#         if year % 400 == 0 :
#             detect = True
#         else :
#             detect = False
#     else :
#         detect = True
# else :
#     detect = False

# if detect :
#     print(f'{year}년은 윤년입니다.')
# else :
#     print(f'{year}년은 평년입니다.')

# Q. 
