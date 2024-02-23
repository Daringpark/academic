import sys
sys.stdin = open('maze_practice.txt')

def maze_start():
    for i in range(16):
        if 2 in maze[i]:
            col = maze[i].index(2)
            row = i
    return row, col

def solve():
    Q = []
    visited = [[0] * 16 for _ in range(16)] # 방문했는지에 관련한 matrix
    visited[start_row][start_col] = 1
    Q.append((maze_start()))
    while Q:
        pos_row, pos_col = Q.pop(0)
        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]: # 시계방향으로 돌면서 갈 곳 체크중
            new_row = pos_row + dr
            new_col = pos_col + dc
            if 0 <= new_row < 16 and 0 <= new_col < 16: # 새로 움직이려고 하는 칸이 범위 내부
                if maze[new_row][new_col] == 3:
                    return 1

                if maze[new_row][new_col] == 0 and not visited[new_row][new_col]:
                    Q.append((new_row, new_col))
                    visited[new_row][new_col] = 1
    return 0

T = 10
for tc in range(1, 11):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    start_row, start_col = maze_start()
    print(f'#{tc} {solve()}')


