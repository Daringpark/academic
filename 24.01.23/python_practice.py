
# 비시퀀스 데이터 구조 (딕셔너리를 위주로)

person = {'Name' : 'Bean', 'Age' : 34, 'Nationality' : 'American'}
print(person)
person.setdefault('Job', 'Chef')
print(person)
person.update({'Job' : 'Officer'})
print(person)
person.update({'Language' : 'English'})
print(person)

# Class와 Dictionary 관리를 통해서 여러 개체를 다룰 수 있을 것이다.

# !!! Hash function에 대한 이해

phone_book = {
    'John' : '512-7494',
    'Lisa' : '512-6457',
    'Kyle' : '512-9475'
}

phone_book_list = [
    {'John' : '512-7494'},
    {'Lisa' : '512-6457'},
    {'Kyle' : '512-9475'}
]

# phone_book_list에서 데이터량이 많을 때 'Lisa'를 찾으려면, 탐색 시간이 늘어남.
# Dictionary의 특성 중 hash function을 이용하면, key 값을 이용하여 빠른 시간에 value를 확인 가능

my_set = {1,34,41,5,60,7,892,912,100}

for i in range(len(my_set)) :
    print(f'#{i} {my_set.pop()}')
print('='*15)

my_set = {1,34,41,5,60,7,892,912,100} # 위 set과 길이가 같은 동일한 set이라 hash의 순서도 같다.
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())

print('='*15)
my_set = {1,34,41,5,60,7,892} #set의 길이가 달라지면, hash 순서도 달라진다.
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())

# int 와 str의 hash difference // int와는 다르게 str은 실행마다 해시값이 변경됨
A = hash(1)
B = hash(1)

print(A, B)
print(A == B)
print(hash('1'))
print(hash('a'))
# 실행을 두 번만 해보아도 기존의 hash 값과 다름을 알 수 있다.

### !!! 결론. '무작위'(random)가 아니라 '임의의'(arbitary) 이다.

# hw_6_2
# 아래 함수를 수정하시오.
def remove_duplicates_to_set(x):

    lst = []

    for number in x :
        if number not in lst :
            lst.append(number)

    lst = set(lst)
    return lst

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

# hw_6_4
# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, *args):
    new_dict = dictionary.copy()
    new_dict.setdefault(*args) # 연속되는 두 인자를 값으로 받음. ('country', 'USA')

    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

## practice ##
# 6_1
# 아래 함수를 수정하시오.

def union_sets(A, B):
    AB = A.union(B)

    return AB

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
# 매개변수 두 개를 사용하는 경우

def union_sets(*args):
    result = set()

    for T in args :
        result = result.union(T)

    return result

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
# 여러 매개변수를 사용 가능하게 만드는 함수 (set타입이 iterable함을 이용함)

# 6_a
my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for k in my_set :
    print(my_dict.get(k))

var = 1,2,3,'A' # 튜플이 키로 설정 가능
my_dict[var] = '변수로도 키 설정 가능'
print(my_dict)

var = 123 # integer를 키로 설정 가능
my_dict[var] = 1
print(my_dict)

# 6_2
# 아래 함수를 수정하시오.
def get_value_from_dict(dictionary, key):
    res = dictionary.get(key)

    return res

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

# 6_b
data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.
print(data.items())

# 2. data가 가진 벨류 목록들만 모아서 출력한다.
print(data.values())

# 3. data에서 'without' 키가 가진 value를 출력한다.
    # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
print(data.get('without', 'Unknown'))

# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
data.update(plus_data)

# 5. 변경된 data를 출력한다.
print(data)

# 6_3
# 아래 함수를 수정하시오.
def intersection_sets(set1, set2):
    
    res = set1.intersection(set2)

    return res

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)

# 6_c
data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']
# 아래에 코드를 작성하시오.

for T in data :
    for key_name in key_list :
        if T.get(key_name) == None :
            T.setdefault(key_name, 'Unknown')
        print(f'{key_name}은/는 {T.get(key_name)}입니다.')
        # 이 위치에서 출력을 해줘야되는데, keys와 values를 깔끔하게 T에서 받을 수 있나?
        # key_list가 주어졌기 때문에, 리스트에서 arguments를 받아서 for문 돌리면 range()를
        # 사용하지 않아도 깔끔하게 작성 가능
    print()

# 6_4
# 아래 함수를 수정하시오.
def get_keys_from_dict(dictionary):
    
    res_list = list(dictionary.keys())

    return res_list

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

# 6_5
# 아래 함수를 수정하시오.
def difference_sets(set1, set2):
    
    A_B = set1.difference(set2)
    return A_B

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)