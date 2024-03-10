
'''
5
1 1 1 6 0
2 7 8 3 1
'''


N = int(input()) # 50 <=
weight = list(map(int, input().split())) # N
weight.sort()
# 0 1 1 1 6
Box = list(map(int, input().split())) # N
# 2 7 8 3 1
Box.sort(reverse=True) # 0 <= w <= 100
# 8 7 3 2 1
# 0 7 3 2 6
sum_value = 0
for i in range(N):
    sum_value += weight[i] * Box[i]
print(sum_value)
