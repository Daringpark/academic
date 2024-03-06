


# R, C <= 500 // 배열을 새로 만들 때 250000 쓰인다
# 2차원 리스트를 2개 만든다? >> 시간 초과 날 것??
# DP는 결국 메모이제이션 문제인 것 같다.
# 어느 위치로 가야할지 정한 것을 재귀한다.
# 알뜰살뜰하게 사용하면 가능할 수도?
# 80% 에서 시간초과

import sys
input = sys.stdin.readline

r, c = map(int, input().strip().split())
Matrix = [list(map(int, input().strip().split())) for _ in range(r)]
drdc = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

def moveable(i, j):
    for 

def lets_go(matrix):
    new_Matrix = [[0] * (c+1) for _ in range(r+1)] # DP 처리
    for row in range(1, r+1):
        for col in range(1, c+1):
            for k in drdc:
                new_Matrix[row][col] = max(new_Matrix[])

    for i in range(r):
        print(*new_Matrix[i])






'''
1 6
10 20 3 4 5 6

4 4
20 2 13 1
4 11 10 35
3 12 9 7
30 40 50 5
'''