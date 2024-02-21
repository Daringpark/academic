### snail array
'''
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''
import sys
sys.stdin = open('1954.txt', 'r')

N = 5
matrix = [list(map(int, input().split())) for i in range(N)]
space = [[0]*N for _ in range(N)]

def findMin(value): #value보다 큰 것 중에서 제일 작은 값 찾기
    minV = 10**10
    for r in range(N):
        for c in range(N):
            if value < matrix[r][c] and minV > matrix[r][c]:
                minV = matrix[r][c]
    return minV
# print(findMin(20)) #21
score = 0
row = 0
col = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
flag = 0

for _ in range(N**2):
    score = findMin(score)
    new_row = row + dr[flag]
    new_col = col + dc[flag]

    space[row][col] = score #값 받기

    if new_row <0 or new_col <0 or new_row >= N or new_col >= N or space[new_row][new_col]:
        flag = (flag+1)%4 # 바운더리 넘지 않기, 값이 있으면, 방향 전환

    row += dr[flag]
    col += dc[flag]

for row in range(N):
    for col in range(N):
        print(space[row][col], end = ' ')
    print()