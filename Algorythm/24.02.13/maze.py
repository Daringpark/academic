import sys
sys.stdin = open('maze.txt')

def find_start():
    for i in range(N):
        if 2 in maze[i]: # 2인 지점이 Start 지점, row 탐색
            j = maze[i].index(2)
            start = [i, j]
            return start
def find_end():
    for i in range(N):
        if 3 in maze[i]: # 3인 지점이 end 지점, row 탐색
            j = maze[i].index(3)
            end = [i, j]
            return end
def solve(start, goal):
    drc = [[-1,0], [0,1], [1,0], [0,-1]] # 시계 방향 확인
    unvisited = [start]
    visited = []
    while unvisited:
        node = unvisited.pop()
        # pos = node
        for i in range(4):
            new_row = node[0] + drc[i][0]
            new_col = node[1] + drc[i][1]
            if 0 <= new_row < N and 0 <= new_col < N and maze[new_row][new_col] != 1:
                # unvisited[new_row][new_col]
                if [new_row, new_col] not in visited:
                    unvisited.append([new_row,new_col])
                if node not in visited:
                    visited.append(node)
            elif maze[new_row][new_col] == 3:
                return 1
    else : return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    print(f'#{tc} {solve(find_start(), find_end())}')