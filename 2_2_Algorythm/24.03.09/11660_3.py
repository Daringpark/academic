
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Matrix = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + Matrix[i-1][j-1]

for m in range(M):
    x, y, end_x, end_y = map(int, input().split()) # x = col, y = row
    print((DP[end_x][end_y] - DP[x-1][end_y] - DP[end_x][y-1] + DP[x-1][y-1]))


'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4

4 1
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
3 4 3 4


'''