

def cross_check(row, col):
    temp = []
    if not visited[row][col]:
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            while (0 <= new_row < N and 0 <= new_col < N):
                if not visited[new_row][new_col]:
                    temp.append((new_row, new_col))
                new_row = new_row + dr
                new_col = new_col + dc
                
        return temp
    return []

def dfs(pos_row, pos_col, hist):
    global cnt

    pass



N = int(input())
matrix = [[0] * N for _ in range(N)]
drdc = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
cnt = 0




for col in range(N):
    visited = [[0] * N for _ in range(N)]
    dfs(0, col, [])