
# # def function

# def make_sum(x, y) : # x, y는 매개 변수 (parameters)
#     return x + y

# A, B = map(int, input().split()) # A, B는 인자 (arguments)

# result = make_sum(A, B)
# print(result)

# # 위치 인자 연습

# def food(food, salt) :
#     print(f'{food}의 염도는 {salt}%입니다.')

# food('김치', 3.3)
# food('김치') # positional argument : 'salt' 위치 인자는 반드시 기입해줘야함.

# #  기본 인자 연습

# def food(food, salt = 1.5) :
#     print(f'{food}의 염도는 {salt}%입니다.')

# food('김치') # 함수 매개 변수를 기본값을 정해주면, 기본 인자 값이 함수 호출한다.
# food('김치', 3.3) # 함수 매개 변수의 값을 정하면, 인자가 바뀐다.

# # 키워드 인자 연습

# def food(food1, food2, daytime = '수요일') :
#     print(f'오늘은 {food1}, {food2}를 드셨군요! 오늘은 {daytime}입니다.')

# food('김치찜', food2 = '곤약젤리')
# # food(food2 = '김치찜', '곤약젤리') # 위치 인자 이후에 키워드 인자가 나와야함. 

# # 여러가지 임의의 인자 (tuple과 dictionary)

# def calculator(*args) :
#     print(args) # 튜플로 저장됨
#     total = sum(args)
#     print(f'총 합은 {total}입니다.')

# calculator(1,2,3,4,5)

# def profiler(**kwargs) :
#     print(kwargs)

# profiler(name = 'Kyle', age = 25, race = 'asian') # 딕셔너리로 저장됨

# # scope (사용자 정의 함수의 변수 범위)
# # Local-Enclosed-Global-Bulitin (LEGB rule)
# a = 1
# b = 2
# # Global arguments

# def enclosed():
#     a = 10
#     c = 3
#     # Enclosed arguments

#     def local(c):
#         print(a, b, c)
#     local(1000) # local argument
#     local(300) # local argument
#     print(a, b, c)

# enclosed() # Enclosed arguments print
# print(a, b) # Global arguments

# # 재귀 함수 연습

# x = int(input())

# def func(i) :
#     if i <= 1 :
#         return 1
#     return i * func(i-1)

# print('팩토리얼을 계산해드립니다. 정수를 기입해보세요. (음수 제외)')
# print(f'팩토리얼의 결과 값은 {func(x)} 입니다.')

# # break rule을 잘 짜는게 중요함.

# # tuple 원소를 갖는 함수, zip()

# A = [1, 2, 3, 4, 5] # [1, 5], 작은 리스트의 길이 만큼만 쌍을 지어 tuple화됨
# B = [3, 4, 5] # [1, 3]

# C = zip(A, B) # [1, 3[1, 2]]
# print(C, type(C), list(C))

# # lambda function (간단한 한 줄 코드를 할 때, 많이 사용됨)

# addition = lambda x, y : x + y

# result = addition(3,5)
# print(result)

# square = lambda x : x ** 2

# result = square(12)
# print(result)

# # 덧셈 함수

# # 아래 함수를 수정하시오.
# def add_numbers(x, y):
#     res = x + y
#     print(f'{x}과 {y}를 인자로 넘긴 경우,\n{res}')

# # 수정한 add_numbers() 함수를 호출하시오.
# add_numbers(3,5)

# #  다양한 built-in function 

# # 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
# negative = -3
# print(abs(negative))

# # 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
# empty_list = []
# print(bool(empty_list))

# # 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))

# # 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
# unsorted_list = ['하', '교', '캅', '의', '지', '가']
# print(sorted(unsorted_list))

# # 3_1 practice

# number_of_people = 0

# def increase_user():
#     global number_of_people
#     number_of_people += 1

# increase_user()
# print(number_of_people)

# # 3_a practice

# def my_multi(number_1, number_2):
#     return number_1 * number_2
# # my_multi(2, 3) 결과 : 6
# # 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.
# result_1 = my_multi(2,3)
# print(result_1)

# def is_negative(number):
#     if number > 0 :
#         return False
#     else :
#         return True
# result_2 = is_negative(3)
# print(result_2)
# # is_negative(3) 결과 : False
# # 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.


# def default_arg_func(default = '기본 값') : #매개변수에 기본 인자를 추가
#     return default

# result_3 = default_arg_func()
# print(result_3)
# result_4 = default_arg_func('다른 값')
# print(result_4)

# # 3_2 practice

# number_of_people = 0

# def increase_user():
#     global number_of_people
#     number_of_people += 1

# print(f'현재 가입 된 유저 수 : {number_of_people}')

# def create_user(name, age, address):
    
#     user_info = {'name' : name , 'age' : age, 'address' : address}
#     print(f'{name}님 환영합니다!')
#     increase_user()
#     return user_info

# print(create_user('홍길동', 30, '서울'))
# print(f'현재 가입 된 유저 수 : {number_of_people}')

# # 3_b practice

# pro_num = 1000
# global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

# def creata_data(subject, day, title = 'None'):
#     global pro_num
#     pro_num += 1
#     data = {}
#     data['과목'] = subject
#     data['일차'] = day
#     data['제목'] = title
#     data['문제 번호'] = pro_num

#     return data

# result_1 = creata_data('python', 3)
# result_2 = creata_data(day = 1, subject = 'web', title = 'web 연습하기')
# result_3 = creata_data(**(global_data)) 
# # dictionary-key-value-keyarguments

# print(f'{result_1}\n{result_2}\n{result_3}')

# # 3_3 practice

# number_of_book = 100

# def decrease_book(n) :
#     global number_of_book
#     number_of_book -= n
#     print(f'남은 책의 수 : {number_of_book}')
# # 정수를 넘겨받는다.
# # 정수만큼 number_of_book을 감소시킨다.
# # 현재 남은 책의 수를 출력한다.

# def rental_book(name, number) :
#     decrease_book(number)
#     print(f'{name}님이 {number}권의 책을 대여하였습니다.')


# rental_book('홍길동', 3)

# # 3_c practice

# def recur_example(number):
#     if number == 1:
#         return 1
#     else:
#         return number + recur_example(number - 1)
# result_1 = recur_example(5)
# print(result_1) # 5 + 4 + 3 + 2 + 1 = 15

# # 거듭 제곱 재귀 함수
# # base = 밑, exponent = 지수
# # base의 exponent승 == 2의 3승
# def power(base, exponent):
#     '''
#         함수(2, 3) 실행
#             base에 2 할당, exponent에 3할당
#             지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

#             아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
#                 2 * 함수(2, 3-1)

#             모든 상황을 반복하는 과정
#             2 * (2 * (2 * 1))  
#             결과 : 8
#     '''
#     if exponent == 0 :
#         return 1
#     else:
#         return base * power(base, exponent -1)
# result_2 = power(2, 3)
# print(result_2) # 2 * 2 * 2 * 1 = 8

# # 모든 자릿수 더하기 함수
# def sum_of_digits(number):
#     '''
#         함수(321) 실행
#         number가 10 미만인 경우, number 반환

#         아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
#             number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
#             1 + (321 // 10)

#         모든 상황을 반복하는 과정
#         1 + 2 + 3
#         결과 : 6
#     '''
#     if number < 10:
#         return number
#     else:
#         return number % 10 + sum_of_digits(number//10)
# result_3 = sum_of_digits(321)
# print(result_3) # 1 + 2 + 3 = 6

# # 3_4 대규모 신규 고객 등록 ### 추가 학습을 해보자!!

# number_of_people = 0

# def increase_user():
#     global number_of_people
#     number_of_people += 1

# def create_user(name, age, address) :
#     user_info = {'name' : name, 'age' : age, 'address' : address}
#     print(f'{name}님 환영합니다!')
#     return user_info

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# def book_user(a,b,c) :
#     return create_user(a, b, c)

# A = list(map(book_user, name, age, address))
# print(A)

# # 3_5 대규모 도서 대여 서비스

number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address) :
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(f'{name}님 환영합니다!')
    return user_info

book_user = lambda a, b, c : create_user(a, b, c)

def change(x) :
    return {'name' : x['name'], 'age' : x['age']}

many_user = list(map(book_user, name, age, address))
info = list(map(lambda x : change(x), many_user))

def rental_book(info):
    global number_of_book
    n = info['age']//10
    user_name = info['name']
    number_of_book -= n
    print(f'남은 책의 수 : {number_of_book}')
    print(f'{user_name}님이 {n}권의 책을 대여하였습니다.')

rental_book(info)

