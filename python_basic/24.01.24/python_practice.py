
### enumerate
# fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits):
#     print(f'인덱스 {index}: {fruit}')


# print(enumerate(fruits))  # <enumerate object at 0x000002133DA99700>
# print(list(enumerate(fruits)))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]





# OOP 1


# hw_7_2
# 아래 클래스를 수정하시오.
# class StringRepeater:

#     def repeat_string(self, num, word) : # def(self)를 받고 다음 parameter를 작성
#         for i in range(num) :
#             print(word)

# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")

# hw_7_4
# 아래 클래스를 수정하시오.
# class Person:
#     number_of_people = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.number_of_people += 1

#     def introduce(self) :
#         print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')

# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)
# person2 = Person("Kyle", 38)
# person2.introduce()
# print(Person.number_of_people)

# ws_7_1
# 아래 클래스를 수정하시오.
# class Shape:

#     def __init__(self, width = 1, height = 1) : # class를 통해 만들어진 인스턴스 생성 이후 첫 매서드
#         self.width = width
#         self.height = height

# shape1 = Shape(5, 3)
# print(shape1.width, shape1.height)

# ws_7_a
# 아래에 코드를 작성하시오.
# my_lsit = [1, 2, 3]
# my_dict = {'A': 1, 'B': 2, 'C': 3}

# print(dir(my_lsit), dir(my_dict), sep = '\n\n', end = '\n\n')
# print(help(my_lsit), help(my_dict), sep = '\n\n')

# ws_7_2
# 아래 클래스를 수정하시오.
# class Shape:
#     width = 1
#     height = 1
#     area = 1

#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height

#     def calculate_area(self) :
#         area = self.width * self.height
#         self.area = area
#         return self.area

# shape1 = Shape(5, 3)
# area1 = shape1.calculate_area()
# print(area1)

# ws_7_b
# 아래에 코드를 작성하시오.
# class Myth :
#     type_of_myth = 0
#     name = 'None'

#     def __init__(self, name):
#         self.name = name
#         Myth.type_of_myth += 1 

#     @staticmethod
#     def description() :
#         print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')

# myth1 = Myth('dangun')
# print(myth1.name)
# myth2 = Myth('greek & rome')
# print(myth2.name)

# print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
# Myth.description()
# # myth1.description() # Class의 Static Method는 당연 하위 생성 instance들에게도 적용된다.
# # myth2.description()

# ws_7_3
# 아래 클래스를 수정하시오.
# class Shape:
#     width = 1
#     height = 1

#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height

#     def calculate_perimeter(self) :
#         surface = 2*self.width + 2*self.height
#         self.surface = surface
#         return self.surface
    

# shape1 = Shape(5, 3)
# perimeter1 = shape1.calculate_perimeter()
# print(perimeter1)

# ws_7_c
# class Car:
#     # 아래에 코드를 작성하시오.
#     wheels = 4

#     def __init__(self, engine, driving_system, sound):
#         self.engine = engine
#         self.driving_system = driving_system
#         self.sound = sound

#     def drive(self) :
#         print(self.sound)
#         return self.engine

#     def introduce(self) :
#         print(f'제 차의 엔진은 {self.engine} 방식 이고, {self.driving_system} (으)로 동작합니다.')

#     @classmethod
#     def increase_wheels(self) :
#         Car.wheels += 1
#         print(f'법이 개정되어 모든 자동차의 필요 바퀴 수가 1 증가하였습니다.')

#     @staticmethod
#     def description() : # 인스턴스와 직접 상호작용하지 않음. 필수 매개변수 없음
#         print('자동차(自動車, 영어: car, automobile)는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통 수단이다.')


# car1 = Car('gasoline', '후륜구동', '부릉부릉')
# car2 = Car('diesel', '전륜구동', '달달달달')
# car3 = Car('hybrid', '4wd', '슈웅')

# car1.drive()
# print(car2.drive())

# print('===')
# car1.introduce()
# car3.introduce()

# print('===')
# print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
# Car.increase_wheels()
# print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
# Car.description()

# ws_7_4
# 아래 클래스를 수정하시오.
# class Shape:

#     def __init__(self, width = 1, height = 1): #setting_default_for_position_args
#         self.width = width
#         self.height = height

#     def print_info(self):
#         print(f'Width: {self.width}')
#         print(f'Height: {self.height}')
#         print(f'Area: {self.width * self.height}')
#         print(f'Perimeter: {2*self.width + 2*self.height}')

# shape1 = Shape(5, 3)
# # shape2 = Shape()
# shape1.print_info()
# # print('=' * 10)
# # shape2.print_info()

# ws_7_5
# 아래 클래스를 수정하시오.
# class Shape:
    
#     def __init__(self, width = 1, height = 1) :
#         self.width = width
#         self.height = height

#     def __str__(self) :
#         return f'Shape: Width = {self.width}, Height = {self.height} '

# shape1 = Shape(5, 3)
# print(shape1)

class Food :
    Food_cnt = 0

    def __init__(self, name, _class, sound = '냠냠'):
        self.name = name
        self._class = _class
        self.sound = sound
        Food.Food_cnt += 1

    def eat(self) :
        # sound = '와작와작'
        # return sound # '와작와작'
        return self.sound # '냠냠'

    def check_food(self) :
        return Food.Food_cnt

Pie = Food('Pie', 'pie')

# print(Pie.name, Pie._class, Pie.sound)
# print(Pie.eat())

# class & def in def practice
# Person이라는 Class를 만든다. Person이라는 클래스를 통해 새 인스턴스 name, code, _class를 인자로 받아, 이름, 학번 그리고 반 이름을 저장한다.
# 인스턴스가 Start()라는 매서드를 사용하면, 





# def time() :
#     hour = 9.0
#     minute = 0.0
#     while True :
#         minute += 0.01

#         if minute >= 3.0 :
#             hour += 1.0
#         if hour >= 24.0 :
#             hour = 0.0
#         return f'{hour} : {minute}' 

# class Person :
#     person_cnt = 0

#     def __init__(self, name, code, _class):
#         self.name = name
#         self.code = code
#         self._class = _class
#         Person.person_cnt += 1

#     # def End(self) :
#     def __str__(self):
#         return f'학생 이름 : {self.name} || 학번 : {self.code} || 반 : {self._class}'

#     def Start(self) :
#         return time()

#     # def Academy(self) :
        
#     @classmethod
#     def number_of_students(cls) :
#         print(f'현재 학생 수는 {cls.person_cnt}명 입니다.')

# p1 = Person('Kyle', 20245135, 'A')
# p2 = Person('Anna', 20242534, 'B')
# print(p1, p2, sep = '\n')
# Person.number_of_students()
# p3 = Person('Betty', 20241782, 'C')
# Person.number_of_students()
# print(p1, p2, p3, sep = '\n')

# while True:
#     print(p1.Start())
#     if p1.hour == 11.0 :
#         break










