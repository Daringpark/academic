import sys
sys.stdin = open('square.txt', 'r')

N = int(input())
space = [[0]*N for i in range(N)] # 정방 행렬 만들기

row, col = map(int, input().split()) # 현재 좌표 받기
L = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

space[row][col] = 1 # 현재 위치
for i in range(4):
    for l in range(1, L+1): # 주어진 길이까지 직선
        new_row = row + dr[i]*l
        new_col = col + dc[i]*l
        # if 0 <= new_row < N and 0 <= new_col < N : # matrix 내에서 그리기 (완)
        #     space[new_row][new_col] = 1
# 내부 구현 해야됨.

for i in range(N):
    for j in range(N):
        print(space[i][j], end = ' ')
    print()