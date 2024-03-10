
import sys
input = sys.stdin.readline

def find(start_row, start_col, end_row, end_col):
    DP = [[0] * N for _ in range(N)]
    if start_row == end_row and start_col == end_col:
        return Matrix[start_row][start_col]

    for i in range(start_row, end_row+1):
        for j in range(start_col, end_col+1):
            if j == end_col:
                DP[i][j] = Matrix[i][j] + DP[i-1][j] + DP[i][j-1]
            else:
                DP[i][j] = Matrix[i][j] + DP[i][j-1]
    return DP[end_row][end_col]

N, M = map(int, input().split())
Matrix = [list(map(int, input().split())) for _ in range(N)]
for m in range(M):
    x, y, end_x, end_y = map(int, input().split()) # x = col, y = row
    print(find(x-1, y-1, end_x-1, end_y-1))