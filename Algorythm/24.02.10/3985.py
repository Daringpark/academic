import sys
sys.stdin = open('input_cake.txt')

# L = int(input())
# real_cake = dict()
# real_cake = list(0 for _ in range(L+1))
# N = int(input())
# fake_max = 0
# fake_number = 0
# real_max = 0
# real_number = 0
# for i in range(1, N+1):
#     start, end = map(int, input().split())   
#     if fake_max < (end-start): # 제일 많이 받을 걸 기대하고 있는 손님 번호 
#         fake_max = end-start
#         fake_number = i
#     for j in range(end-start+1): # 실제로 많이 받을 손님 번호
#         if real_cake[start+j] == 0:
#             real_cake[start+j] = i
#         counts = real_cake.count(i)
#         if real_max < counts :
#             real_max = counts
#             real_number = i
# print(fake_number)
# print(real_number)

###################################

# 첫 저장을 딕셔너리로 저장하는 것이 의미가 있다. 124ms
import sys
input = sys.stdin.readline # readline으로 64ms
L = int(input())
N = int(input())
real_cake = dict()
fake_max = 0
fake_number = 0
for i in range(1, N+1):
    start, end = map(int, input().split())  
    l = end - start + 1
    for j in range(l):
        if start+j not in real_cake:
            real_cake[start+j] = i
    if fake_max < (end-start): # 제일 많이 받을 걸 기대하고 있는 손님 번호 
        fake_max = end-start
        fake_number = i
real_max = 0
real_number = 0
for j in set(real_cake.values()):
    counts = list(real_cake.values()).count(j)
    if real_max < counts:
        real_max = counts
        real_number = j
print(f'{fake_number}\n{real_number}')


