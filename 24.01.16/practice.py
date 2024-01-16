
# f-string 이해하기
print(f'다음은 이형기 시인의 \"낙화\"의 한 구절이다.\n- 1연\n	가야할 때 언제인가를\n	분명히 알고 가는 이의\n	뒷모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.')

# type 변환 (명시적 형변환)
book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
book = int(book)
print(guide)
print(book * total)

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
rental = int(rental)
print(changes)
print(total - rental)

# type 변환 (중복제거, 명시적 형변환)
list_A = ['사과', '배', '사과', '포도', '감', '수박', '사과', '포도']
print(list_A)

list_A = set(list_A) #set()형변환을 이용하여, 중복된 값을 제거해준다. set()은 집합 변수
print(list_A, type(list_A))

list_A = list(list_A) #set()으로 되어있는 list()형변환을 이용하여 다시 list 형태로 바꿔준다.
print(list_A, type(list_A))

# 리스트 활용하기

zero_list = [0]
print(zero_list)
many_zero_list = [0]*250000
print(len(many_zero_list))
numbers = list(range(1,11))
print(numbers)
print(numbers[3:])

# 숫자형 변수 = 0이 아닌 숫자에는 n(True)으로 본다.
# 문자형 변수 = ''(공백)이 아니면, 문자가 있다고(True)로 본다.
# 리스트형 변수 = []는 0이고, 차있는 리스트는 True로 본다.

