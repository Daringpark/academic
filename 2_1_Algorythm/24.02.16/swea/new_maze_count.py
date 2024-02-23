import sys
sys.stdin = open('new_maze_count.txt')

def find_start():
    for i in range(N):
        if 2 in maze[i]:
            return i, maze[i].index(2)
def solve():
    Q = []
    Q.append((start_row,start_col))
    visited = [[0]*N for _ in range(N)] # 초기 위치는 0으로 count 시작

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while Q:
        row, col = Q.pop(0)
        for i in range(4): # 시계방향으로 돌리기
            new_row = row + dr[i]
            new_col = col + dc[i]
            if 0 <= new_row < N and 0 <= new_col < N:
                if maze[new_row][new_col] == 3:
                    return visited[row][col]
                if maze[new_row][new_col] != 1 and not visited[new_row][new_col]:
                    Q.append((new_row, new_col))
                    visited[new_row][new_col] = visited[row][col] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start_row, start_col = find_start()
    print(f'#{tc} {solve()}')