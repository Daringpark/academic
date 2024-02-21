
# 자료구조와 알고리즘

# find

my_string = 'korean and English'

my_string = my_string.capitalize()
print(my_string)

print(my_string.index('K'), my_string.index('a'))

K = 'Korean'
E = 'ENGLISH'
J = 'japanese'

print(K.isupper())
print(E.isupper())
print(J.islower())

text = '      Hello! My Little man!          '
text = text.strip()
print(text)
text = text.replace('Hello', 'Howdy')
print(text)
text = text.strip('Howdy!'); text = text.strip() #느낌표가 사라짐
print(text)

# Method Chaining시, None.method()를 진행하면 Error를 띄운다.

# 베커스-나우르 표기법 ???

# Insert()
numbers = [0,1,2,3,4]
numbers.insert(1,5) # insert(1번 위치에 5를 넣어주기)
print(numbers)

# pop()은 return 값이 존재하다.
A = numbers.pop()
B = numbers.pop(2)

print(A, B)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)

# sort()는 return 값이 존재하지 않음. == 원본 리스트가 변경됨.

# 얕은 복사 (Narrow Copy), 1차원 리스트 공간에서는 사용 가능하지만, 고차원일 경우, 원하는 결과를 뽑지 못함
a = [1,2,3,4]
b = a[:]
print(a, b)
b[2] = 4
b[3] = 5
print(a,b)

a = [0, 1, [1,2,3,4]]
b = a[:]
print(a, b)
b[2][3] = 100; b[1] = 10 #b[1]은 1차원 리스트 내에 존재하기에 b 단일로 변경되었지만, 2차원 리스트의 값은 같이 변경됨
print(a, b)

# hw_5_2
# 아래 함수를 수정하시오.
def count_character(Word, alpa):
    
    A = []
    for i in range(len(Word)) :
        A.append(Word[i])

    cnt = A.count(alpa)
    return cnt

result = count_character("Hello, World!", "o")
print(result)  # 2
# dictionary의 key and value이면 오히려 더 깔끔할 수 있을텐데...

# hw_5_4
# 아래 함수를 수정하시오.
def find_min_max(numbers):
    
    numbers.sort()
    A = numbers[0]
    B = numbers[-1]
    return A, B

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)

# 5_1
# 아래 함수를 수정하시오.
def reverse_string(Word):

    # A = []
    # for i in range(len(Word)) :
    #     A.append(Word[i])
    
    # A.reverse()
    # sentence = ''.join(A)

    # return sentence

    Word = list(reversed(Word))
    sentence = ''.join(Word)
    
    return sentence

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

# 5_a
N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for i in range(N) :
    arr_1.append(data_1[i])
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
arr_2 = list(map(int, data_2.split()))
for j in range(M) :
    if arr_2[j] % 2 != 0 :
        print(arr_2[j])

# 5_2
# 아래 함수를 수정하시오.
def remove_duplicates(lst):
    new_lst = []
    
    for i in range(len(lst)) :
        if lst[i] not in new_lst :
            if lst[i] in lst : new_lst.append(lst[i])

    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

# 5_2 ## 강사님 풀이
def remove_duplicates(lst):
    new_lst = []
    
    for number in lst :
        if number not in new_lst :
            new_lst.append(number)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

# 5_b
data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
for letter in data_1 :
    if letter.isupper() != 0 or letter == ' ' :
        print(letter, end = '')

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
A = data_2.find('내')
B = data_2.find('힘')
C = data_2.find('들')
D = data_2.find('다')
arr.append(A); arr.append(B); arr.append(C); arr.append(D)
print(f'\n{arr}')
arr.sort()
print(arr)
for i in arr :
    print(data_2[i], end = '')

## 강사님 풀이
data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
for letter in data_1 :
    if letter.isupper() != 0 or letter == ' ' :
        print(letter, end = '')

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
txt = '내힘들다'

for c in txt :
    a = data_2.find(c)
    arr.append(a)
print()
print(arr)
arr.sort()
print(arr)
for i in arr :
    print(data_2[i], end = '')
print()

# 5_3
# 아래 함수를 수정하시오.
def sort_tuple(A):
    new_tuple = ()
    (A := list(A)).sort()
    new_tuple = tuple(A)

    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)

## sorted()
def sort_tuple(A):
    new_tuple = ()

    return tuple(sorted(A))
result = sort_tuple((5, 2, 8, 1, 3))
print(result)

# 5_c
# 아래 함수를 수정하시오.

def restructure_word(word, arr):

    for i in word :
        if i.isdecimal() : # 자체적으로 True니까
            for _ in range(int(i)) : arr.pop(-1)
        else :
            arr.remove(i)
    return arr
# isdecimal() = True, 1,2,3,4,5 -> original_word의 특수문자 15개를 제거
# remove(i) = 필요 없는 ㄴ,ㄹ,ㅓ,ㅅ 를 original_word에서 제거

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

for letter in original_word :
    arr.extend(letter)
print(arr)

result = restructure_word(word, arr)
print(result)
print(''.join(result))

# 5_4
# 아래 함수를 수정하시오.
def capitalize_words(word):
    arr = []
    arr.extend(word.split())
    arr_1 = []

    for i in arr :
        arr_1.append(i.capitalize())
    return ' '.join(arr_1)

result = capitalize_words("hello, world!")
print(result)

# 5_5
# 아래 함수를 수정하시오.
def even_elements(lst):
    num_list = []
    while lst :
        lst.pop(0)
        if lst[0] % 2 == 0 :
            num_list.extend([lst[0]])
            lst.pop(0)
    return num_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)






