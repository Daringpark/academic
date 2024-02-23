import sys
sys.stdin = open('input_p3.txt', 'r')

T = int(input())
N, M = map(int, input().split()) # 최대 범위
pos = list(map(int, input().split())) # 현재 포지션
di = [-1, 1]
dj = [-1, 1]


for _ in range(T):
    order = int(input())
    if order < 2:
        pos[0] += di[order]
    else :
        pos[1] += dj[order-2]

    if 0 <= pos[0] < N and 0 <= pos[1] < M:
        print(order, pos)
    else :
        print('Fail')
        break


