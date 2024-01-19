
# # 숙제 안낸 사람?
## 44ms , 108 B

# Bag = list(range(1, 31))

# for _ in range(28) :
#     Bag.remove(int(input()))
# print(f'{Bag[0]}\n{Bag[1]}')

## 두 개의 반복문으로 찾기; one-hot-encoding
## 44ms , 130 B

# Bag = [0] * 30

# for i in range(28) : 
#     Bag[int(input()) -1] += 1
# for j in range(30) :
#     if Bag[j] != 1 :
#         print(j + 1)

# # 학점 계산기

# list_GPA = [['D+', 'D0', 'D-'], ['C+', 'C0', 'C-'], ['B+', 'B0', 'B-'], ['A+', 'A0', 'A-']]

# n = len(list_GPA)
# x = input()
# for i in range(n) :
#     m = len(list_GPA[i])
#     for j in range(m) :
#         if x in list_GPA[i][j] :
#             res = i + 1.0
#             if j > 1 :
#                 res -= 0.3
#             elif j <= 0 : 
#                 res += 0.3
#         elif x == 'F' :
#             res = 0.0
# print(res)

# ## 처리 시간 -, 코드 길이 -

# scores = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
# score = input()
# print(scores[score])

# # 개수 세기

# n = int(input())
# A = list(map(int, input().split()))
# number = int(input())
# if number in A :
#     print(A.count(number))
# else : 
#     print(0)

# input()
# print(input().split().count(input()))


# # 문자와 문자열 (읽기)

# word = input()
# n = int(input())
# print(word[n - 1])

# print(input()[int(input()) -1])

# # 구구단

# N = int(input())

# for i in range(1, 10) :
#     print(f'{N} * {i} = {N * i}')

