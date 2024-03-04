import sys
# sys.stdout = open("10163.txt", "w")
import sys
input = sys.stdin.readline

# N = int(input())
# Matrix = [[0] * 1002 for _ in range(1002)]
# for n in range(N):

#     start_x, start_y, width, height = map(int, input().split()) # 1,2 >> # 999, 1

#     for i in range(height):
#         for j in range(width):
#             Matrix[1001-start_y-i][start_x-1+j] = n+1
# # for i in range(1002):
# #     print(*Matrix[i])
# for k in range(N):
#     cnt = 0
#     for i in range(1002):
#         for j in range(1002):
#             if Matrix[i][j] == k+1:
#                 cnt += 1
#     print(cnt)

import sys
input = sys.stdin.readline

Matrix = [[0 for _ in range(1002)] for _ in range(1002)]
N = int(input())

for p in range(1, N+1):
    p_x, p_y, width, height = map(int, input().split())
    for y in range(p_y, p_y+height):
        Matrix[y][p_x:(p_x+width)] = [p]*width # 한번에 바꿔야된다. 아오
            
for p in range(1, N+1):
    result = 0
    for cnt in range(1002):
        result += Matrix[cnt].count(p)
    print(result)