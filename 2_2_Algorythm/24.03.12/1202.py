
from collections import deque

N, K = map(int, input().split())
# N = 보석의 개수
# K = 가방의 개수
jewel = []
for i in range(N):
    jewel.append(list(map(int, input().split()))) # 무게와 가격
bags = []
for i in range(K):
    bags.append(int(input()))
# Quick sort를 써야할 것 같음.
# 일반 정렬은 시간이 오래걸릴 것 같고
# list에서 sort method 이후에 queue 전환해도 상관 없긴 할 듯
    
# 뭔가 가방 무게랑 매칭이 안될 수도 있음
# O(NK)이면 9 * 10**10 2*10**7
bags.sort(reverse=True) # 얘까지는 오케이
bags = deque(bags)

print(jewel, bags)


'''
2 2
5 10
100 100
50
11
'''