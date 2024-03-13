

from collections import deque
# N, K 
# weight, wealth
# K weight limit
N, K = map(int, input().split())
jewels = []
for _ in range(N):
    jewels.append(list(map(int, input().split())))
jewels.sort(key = lambda x : (-x[1], x[0])) # 값을 기준으로 무게를 정렬한다?
# jewels = deque(jewels)
print(jewels)


bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort(reverse=True)




'''
3 2
1 65 >> 2
5 23
2 99 >> 1
10
2
'''




