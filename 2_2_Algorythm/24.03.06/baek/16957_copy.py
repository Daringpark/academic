import sys
input = sys.stdin.readline

r, c = map(int, input().strip().split())
Matrix = [list(map(int, input().strip().split())) for _ in range(r)]
new_Matrix = [[0] * c for _ in range(r)]
direction_list = [[0] * c for _ in range(r)]
drdc = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for row in range(r):
    for col in range(c):
        min_val = Matrix[row][col]
        min_row, min_col = row, col
        for dr, dc in drdc:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < r and 0 <= new_col < c:
                if Matrix[new_row][new_col] < min_val:
                    min_val = Matrix[new_row][new_col]
                    min_row, min_col = new_row, new_col
        if min_row != row or min_col != col:
            direction_list[min_row][min_col] = [row, col]

for i in range(r):
    for j in range(c):
        X = direction_list[i][j]
        while X != 0:
            x, y = X[0], X[1]
            X = direction_list[x][y]
        if X == 0:
            new_Matrix[x][y] += 1

for i in range(r):
    print(*new_Matrix[i])
