import sys
sys.stdin = open('maze.txt')

def find_start():
    for i in range(N):
        if 2 in maze[i]: # 2인 지점이 Start 지점, row 탐색
            return [i, maze[i].index(2)]
def solve(start):
    drc = [[-1,0], [0,1], [1,0], [0,-1]] # 시계 방향 확인
    stack = [start]
    while stack:
        node = stack.pop()
        for i in range(4): # for문 밖으로 빼서 연산을 하는 경우, 새로운 위치를 탐색하여 stack에 저장
            new_row = node[0] + drc[i][0]
            new_col = node[1] + drc[i][1]
            if 0 <= new_row < N and 0 <= new_col < N and maze[new_row][new_col] != 1:
                stack.append([new_row, new_col])
        if maze[node[0]][node[1]] == 3: # 조기 종료
            return 1
        maze[node[0]][node[1]] = 1 # visited하면 해당 0을 1로 변환
    else : return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    print(f'#{tc} {solve(find_start())}')