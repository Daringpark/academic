
# 10828번 스택
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 3003번 체스 말 갯수 맞추기
# import sys
# input = sys.stdin.readline

# chess_box = [1, 1, 2, 2, 2, 8]
# check_box = list(map(int, input().split()))

# for i in range(len(chess_box)) :
#     if check_box[i] == chess_box[i] :
#         check_box[i] = 0
#     else :
#         check_box[i] = chess_box[i] - check_box[i]
#     print(check_box[i], end = ' ')

# 4796번 캠핑 ## 44ms
# import sys
# input = sys.stdin.readline

# cnt = 1
# while True :
#     try :
#         L, P, V = map(int, input().split())
#         res = V%P 
#         N = V//P

#         if res > L:

#             result = (N + 1) * L
#             print(f'Case {cnt}: {result}')
#         elif res <= L :
            
#             result = N * L + res
#             print(f'Case {cnt}: {result}')

#         cnt += 1
#     except ZeroDivisionError:
#         break

# 2563번 색종이
# import sys
# input = sys.stdin.readline # 이거 추가해서 56ms

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

# 1157번 : 단어 공부
word = 'Mississipi'
word = word.upper()

word = list(map(str, word))
letter_dict = dict()

for letter in word :
    letter_dict



