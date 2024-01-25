
### enumerate
# fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits):
#     print(f'인덱스 {index}: {fruit}')


# print(enumerate(fruits))  # <enumerate object at 0x000002133DA99700>
# print(list(enumerate(fruits)))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]



### OOP 2

# 클래스 상속하기 (활용 연습)

# class Person :
#     expense = 1000

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self) :
#         print(f'반갑습니다. {self.name}입니다.')

#     def shake(self) :
#         print(f'{self.name}은 손을 흔들었습니다.')

#     def card_tag(self) :
#         if self.age >= 65 :
#             print(f'{self.age}는 65세 이상으로 무료로 탑승 가능합니다.')
#         elif 15 < self.age < 65 :
#             print(f'연령에 맞는 요금을 지불하세요. {self.expense}를 지불하세요.')

#     @classmethod
#     def increase_expense(cls) :
#         cls.expense += 200
#         print(f'법 개정으로 인해서 기존 요금보다 200원 더 비싸졌습니다. 현재 요금 : {cls.expense}')

# class Student(Person) :

#     expense = int(Person.expense * 0.7)

#     def __init__(self, name, age, _class, school, number):
#         super().__init__(name, age)
#         self._class = _class
#         self.school = school
#         self.number = number
    

#     def check(self) :
#         print(f'{self.name}은 {self.school}에 다니고 있습니다.')
#         print(f'학급 반과 번호는 {self._class}, {self.number}입니다.')

# class Professor(Person) :

#     expense = int(Person.expense * 0.95)

#     def __init__(self, name, age, department, period):
#         super().__init__(name, age)
#         self.department = department
#         self.period = period

#     def check(self) :
#         print(f'{self.name}은 {self.department}의 교수입니다.')
#         print(f'{self.department}에 계신지 {self.period}개월 되셨습니다.')

# st1 = Student('김철수', 16, 'A', '무진고등학교', 2468)

# pr1 = Professor('김현수', 34, 'Physics', 40)
# pr2 = Professor('이주협', 42, 'Economics', 110)

# pr2.check()
# Person.increase_expense()
# print(Person.expense)

# # pr2.card_tag()
# # Person.increase_expense()
# # Person.increase_expense()
# st2 = Student('박민수', 18, 'C', '무진고등학교', 1675)
# st1.card_tag()
# st2.card_tag()
# # 업데이트 함수가 없어?



# hw_8_2
# 아래 함수를 수정하시오.
# def check_number():
#     while True : 
#         try :
#             num = int(input('숫자를 입력하세요 : ')) 
#             if num > 0 :
#                 print('양수입니다.')
#             elif num < 0 :
#                 print('음수입니다.')
#             else :
#                 print('0입니다.')

#         except :
#             print('잘못된 입력입니다.')
#             break

# check_number()
# 잘못된 입력이 들어오기 전까지 계속 판별해주게 코드를 작성함.

# hw_8_4
# 아래 클래스를 수정하시오.
# class UserInfo:
#     def __init__(self):
#         self.user_data = {}

#     def get_user_info(self):
#         try :
#             self.user_data['name'] = input('이름을 입력하세요 : ')
#             self.user_data['age'] = int(input('나이를 입력하세요 : '))
#         except ValueError :
#             print(f'나이는 숫자로 입력해주세요.')
       
#     def display_user_info(self):
#         try :
#             print(f'사용자 정보 :\n이름 : {self.user_data["name"]}\n나이 : {self.user_data["age"]}')
#         except KeyError :    
#                 print('사용자 정보가 입력되지 않았습니다.')
#         # if self.user_data["name"] == '' :
#         #     print('사용자 정보가 입력되지 않았습니다.')
 
# user = UserInfo()
# user.get_user_info()
# user.display_user_info()

# ws_8_1
# 아래 클래스를 수정하시오.
# class Animal:
#     number_of_animal = 0

# class Dog(Animal):
#     def __init__(self):
#         Animal.number_of_animal += 1

# class Cat(Animal):
#     def __init__(self):
#         Animal.number_of_animal += 1

# # 문제의 의도인지 모르겠지만, Class Dog, Cat을 수정하라고 했다.
# # 부모 클래스를 받는거 자체가 클래스 수정이라고 보면 Animal에 init에 ++을 넣어주면 된다.
# # super 혹은 Animal 자체에서 cnt을 ++ 해주는 게 좋다.
# class Pet(Cat, Dog):
    
#     @classmethod
#     def access_num_of_animal(cls) :
#         return f'동물의 수는 {cls.number_of_animal}마리 입니다.'
# # 부모 클래스로 올라간다. Pet > Cat > Animal, Pet > Dog > Animal [다이아몬드 구조]

# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

# ws_8_a
# # data = {'name': '홍길동'}
# # if not data['age']:
# #     print(data['age'])
# # else:
# #     print('data에는 age라는 키가 없습니다.')
# #     data['age'] = 30
# #     print(data)
# # 아래에 코드를 작성하시오.
# data = {'name': '홍길동'}
# try :
#     print(data['age'])
# except KeyError :
#     print('data에는 age라는 키가 없습니다.')
#     data['age'] = 30
#     print(data)

# # arr = ['반갑', '하세요', '안녕']
# # for i in range(4):
# #     print(arr.pop())
# # print(arr)
# # 아래에 코드를 작성하시오.
# arr = ['반갑', '하세요', '안녕']
# for i in range(4):
#     try :
#         print(arr.pop())
#     except IndexError :
#         print(arr)
#         print('더 이상 pop 할 수 없습니다.')

# # word = '3.15'
# # print(int(word))
# # # 아래에 코드를 작성하시오.
# word = '3.15'
# try :
#     print(int(word))
# except ValueError :
#     print(f'정수로 변환 가능한 값을 입력해 주세요.')

# ws_8_2
# 아래 클래스를 수정하시오.
# class Animal:
#     number_of_animal = 0

#     def __init__(self):
#         Animal.number_of_animal += 1

# class Dog(Animal):

#     def bark(self) :
#         print('멍멍!')

# dog1 = Dog()
# dog1.bark()

# ws_8_b
# class BaseModel:
#     PK = 1
#     TYPE = 'Basic Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         self.PK = BaseModel.PK
#         self.data_type = data_type 
#         self.title = title 
#         self.content = content 
#         self.created_at = created_at 
#         self.updated_at = updated_at
#         BaseModel.PK += 1
    
#     def save(self):
#         print('데이터를 저장합니다.')

# class Novel(BaseModel):
    
#     def __init__(self, data_type, title, content, created_at, updated_at, author):
#         super().__init__(data_type, title, content, created_at, updated_at)
#         self.author = author
    
# class Other(BaseModel):

#     TYPE = 'Other Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         super().__init__(data_type, title, content, created_at, updated_at)
    
#     def save(self):
#         print('데이터를 다른 곳에 저장합니다.')

# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
# print(hong.PK)
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()

# print('---')
# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other.TYPE)

# ws_8_3
# 아래 클래스를 수정하시오.
# class Animal:
#     number_of_animal = 0

#     def __init__(self):
#         Animal.number_of_animal += 1

# class Dog(Animal):

#     def bark(self) :
#         print('멍멍!')

# dog1 = Dog()
# dog1.bark()

# class Cat(Animal):
    
#     def __init__(self, sound):
#         super().__init__()
#         self.sound = sound

#     def meow(self) :
#         print(f'{self.sound}!')

# cat1 = Cat("야옹")
# cat1.meow()

# ws_8_c
# class BaseModel:
#     PK = 1
#     TYPE = 'Basic Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         self.PK = BaseModel.PK
#         self.data_type = data_type 
#         self.title = title 
#         self.content = content 
#         self.created_at = created_at 
#         self.updated_at = updated_at
#         BaseModel.PK += 1
    
#     def save(self):
#         print('데이터를 저장합니다.')

# class Novel(BaseModel):
    
#     def __init__(self, data_type, title, content, created_at, updated_at, author):
#         super().__init__(data_type, title, content, created_at, updated_at)
#         self.author = author

# class Other(BaseModel):

#     TYPE = 'Other Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         super().__init__(data_type, title, content, created_at, updated_at)
    
    # def save(self):
    #     print('데이터를 다른 곳에 저장합니다.')

# class ExtendedModel(Novel, Other):

#     extended_type = 'Special Model'

#     def __init__(self, data_type, title, content, created_at, updated_at, author):
#         super().__init__(data_type, title, content, created_at, updated_at, author)
#         self.title = None
#         self.author = None

#     def display_info(self) :
#         print(f'PK : {self.PK}')
#         print(f'TYPE : {self.TYPE}')
#         print(f'extended_type : {self.extended_type}')

#     def save(self) :
#         print('데이터를 확장해서 저장합니다.')

# extended_instance = ExtendedModel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# extended_instance.display_info()
# extended_instance.save()

# print(f'Data_Type : {extended_instance.data_type}\nTitle : {extended_instance.title}\nContent : {extended_instance.content}')

# ws_8_4
# 아래 클래스를 수정하시오.
# class Animal:
#     number_of_animal = 0

#     def __init__(self):
#         Animal.number_of_animal += 1

# class Dog(Animal):

#     def bark(self) :
#         print('멍멍!')

# class Cat(Animal):
    
#     def __init__(self, sound):
#         super().__init__()
#         self.sound = sound

#     def meow(self) :
#         print(f'야옹!')

# class Pet(Dog, Cat):

#     def __init__(self, sound):
#         super().__init__(sound)

#     def play(self) :
#         print(f'애완동물과 놀! 기!')

#     def make_sound(self) :
#         print(self.sound)

# pet1 = Pet("그르르") #init에서 받은 sound를 기준으로 
# pet1.make_sound() # Cat class의 sound parameter를 받아서 pet instance의 self.sound를 낸다.
# pet1.bark() # Pet > Dog 의 instance method bark()를 받아서 호출
# pet1.meow() # Pet > Dog에서 먼저 찾아보고 호출할 것이 없으니
#             #Pet > Cat의 instance method meow()를 받아서 호출
# pet1.play() # Pet의 instance method play()를 받아서 호출

# ws_8_5
# 아래 클래스를 수정하시오.
# class Animal:
#     number_of_animal = 0

#     def __init__(self):
#         Animal.number_of_animal += 1

# class Dog(Animal):

#     sound = '멍멍'

#     def __init__(self):
#         super().__init__()

#     def bark(self) :
#         print('멍멍!')
    

# class Cat(Animal):
    
#     sound = '야옹'

#     def __init__(self):
#         super().__init__()

#     def meow(self) :
#         print(f'{self.sound}!')

# # class Pet(Dog, Cat):
# class Pet(Cat, Dog): # 위 아래 주석처리를 통해서 먼저 호출되는 순서를 바꿀 수 있다.

#     def __init__(self):
#         super().__init__()

#     def play(self) :
#         print(f'애완동물과 놀! 기!')

#     def __str__(self):
#         return f'애완동물은 {self.sound} 소리를 냅니다.'

# p1 = Pet()
# print(p1)

