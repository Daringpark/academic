
# 10828번 스택
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# import sys
# input = sys.stdin.readline

# Test_case = int(input())
# stack_list = []

# for i in range(Test_case) :
#     Order = list(map(str, input().split()))
#     M = len(Order)

#     if M >= 2 :
#         stack_list.append(int(Order[1]))
#     else :
#         N = len(Order[0])
#         if N >= 5 :
#             if len(stack_list) == 0 :
#                 print(1)
#             else :
#                 print(0)
#         elif N >= 4 :
#             print(len(stack_list))
#         else :
#             if Order[0] == 'top' :
#                 if len(stack_list) == 0 :
#                     print(-1)
#                 else : 
#                     print(stack_list[-1])
#             else :
#                 if len(stack_list) == 0 :
#                     print(-1)
#                 else : 
#                     print(stack_list[-1])
#                     stack_list.pop(-1)

# 10814번 나이순 정렬
# import sys
# input = sys.stdin.readline

# N = int(input())
# PersonList = []
# for i in range(N) :
#     person = list(map(str, input().split()))
#     PersonList.append(person)

# for i in range(N) :
#     PersonList[i]
#     print(' '.join(PersonList[i]))
# 실패 // 가입한 순서대로가 아님 << sort로 풀이하는게 아니다.
# 그럼 어떻게? 딕셔너리 키와 밸류로. 나이는 key값을 받고, value로 사람 이름을 넣어준다. append 형식

#### 중요 !!!!!
import sys
input = sys.stdin.readline

N = int(input())
person_dictionary = {}

for i in range(N) :
    person_age , person_name = map(str, input().split())
    if person_age not in person_dictionary :
        person_dictionary[person_age] = [person_name]
    else :
        person_dictionary[person_age].append(person_name)

Age_key = list(person_dictionary.keys()) # key를 리스트로 저장
# print(Age_key)
for age in Age_key :

    for j in len(person_age[age].values()) :
        print(f'{age} ')
# {Age_key[age]}


# print(person_dictionary)
        





