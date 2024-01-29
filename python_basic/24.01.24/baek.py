
# 9086번 문자열
# T = int(input())

# for i in range(T) :
#     word = input()
#     print(word[0], word[-1], sep = '')

# 2743번 단어 길이 재기
# word = input()
# if len(word) <= 100 : 
#     print(len(word))

# 2744번 대소문자 바꾸기
# word = input()
# if len(word) <= 100 :
#     print(word.swapcase())

# 1259번 팰린드롬수
### 44ms
# word = None
# while word != '0' :
#     word = input()
#     if word[::-1] == word and word != '0':
#         print('yes')
#     elif word == '0' :
#         break
#     else :
#         print('no')

# 약수 만들기
# T = int(input())
# num_list = []

# for i in range(1, T+1) :
#     if T % i == 0 :
#         num_list.append(str(i))

# 1978번 소수 찾기
# T = int(input())
# lst = list(map(int, input().split()))
# cnt = 0

# for i in lst :
#     num_list = []
#     for j in range(1, i+1) :
#         if i % j == 0 :
#             num_list.append(str(j))
#     # print(num_list)
#     if len(num_list) == 2 :
#         cnt += 1
# print(cnt)

# 1546번 평균
# T = int(input())

# num_list = list(map(int, input().split()))
# new_list = []

# for number in num_list :
#     new_list.append(number/max(num_list) * 100)
# print(sum(new_list)/T)

# 11050번 이항 계수 1
# 44ms
# N, K = map(int, input().split())

# mother_list = []
# son_list = []
# res = 1

# for i in range(K) :
#     mother_list.append(int(N - i))
#     son_list.append(int(i + 1))

#     res = res * (mother_list[i] / son_list[i])
# print(int(res))

# combination의 메인 컨셉 // 40ms
# def f(n):
#     if n == 0:
#         return 1
#     return n * f(n-1)
# n, m = map(int, input().split())
# print(f(n)//f(n-m)//f(m))

# 1181번 단어 정렬
# 900ms
# T = input()

# A = []
# for i in range(int(T)) :
#     A.append(input())

# total = []
# for i in range(1, 51) :
#     lnth_list = []
#     for j in A :
#         if len(j) == i :
#             lnth_list.append(j)
#     lnth_list = list(set(lnth_list))
#     lnth_list.sort()
#     if len(lnth_list) >= 1 :
#         total.extend(lnth_list)

# print('\n'.join(total))

# 64ms
# import sys
# input = sys.stdin.readline

# Nword = []
# N = int(input())

# for _ in range(N) :
#     word = input().strip()
#     Nword.append(word)
    
# total = list(set(Nword))
# total.sort()
# total.sort(key = len)

# print("\n".join(total))

# 2609번 최대공약수와 최소공배수
# M, N = map(int, input().split())
# num_list_1 = []
# num_list_2 = []

# for i in range(1, M+1) :
#     if M % i == 0 :
#         num_list_1.append((i))
# # print(num_list_1)

# for i in range(1, N+1) :
#     if N % i == 0 :
#         num_list_2.append((i))
# # print(num_list_2)

# ANB = set(num_list_1).intersection(set(num_list_2))
# print(max(ANB))
# print(num_list_1[-1]//max(ANB)*num_list_2[-1])

# 1037번 : 약수
# T = int(input())
# num_list = sorted(list(map(int, input().split())))

# print(min(num_list)*max(num_list))

# 10828번 스택
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.






