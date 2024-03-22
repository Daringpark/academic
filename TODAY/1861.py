

from collections import deque

def bfs(start):
    
    # 첫 시작을 잡아서 탐색 돌기
    start_r, start_c = start
    q = deque([[start_r, start_c]])
    visited[start_r][start_c] = 1
    if not table[start_r][start_c]:
        table[start_r][start_c] = [1, matrix[start_r][start_c]]
    
    while q:
        row, col = q.popleft()
        
        for dr,dc in drdc: # 탐색을 하고자 한다.
            new_r = row + dr
            new_c = col + dc
            
            if 0 <= new_r < N and 0 <= new_c < N: # 근처에 있는게 일단, 범위 내에 있는지
                if not visited[new_r][new_c]: # 내딛을 위치가 첫 방문인가?                    
                    if matrix[row][col] + 1 == matrix[new_r][new_c]: # 조건에 부합하다면
                        visited[new_r][new_c] = 1
                        table[row][col][0] += 1
                        table[new_r][new_c] = table[row][col]
                        q.append([new_r, new_c])
                    
                # else: # 방문한 적이 있었다면?
                #     if matrix[row][col] +1 == matrix[new_r][new_c]:
                #        visited[new_r][new_c][0] += visited[row][col][0]
                #        visited[new_r][new_c][1] = min(visited[new_r][new_c][1], visited[row][col][1])
                #        q.append([new_r, new_c])
                
                # # 조건 체크 : 내가 지금 visited에 가지고 있는 값이 내가 내 딛어야 할 칸의
                # if not visited[new_r][new_c] or visited[row][col][0] > visited[new_r][new_c][0]:
                #     if matrix[row][col] + 1 == matrix[new_r][new_c]: # 조건 : 내가 가야할 값이 1 이상인지
                #         visited[row][col][0] += 1
                #         visited[new_r][new_c] = visited[row][col]
                #         q.append([new_r, new_c])

# 연결성이 4?

drdc = [[-1,0], [0,1], [1,0], [0,-1]]
T = int(input())
for tc in range(1, T+1):
    
    N = int(input()) # N = 1e3
    # 1e6 matrix
    # 값도 1e6,  1e12
    matrix = [list(map(int, input().split())) for _ in range(N)]
    table = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            bfs([i,j]) # 완탐을 돌면서 갱신
            for k in range(N):
                print(*table[k])
    
    max_value = 0
    min_number = int(1e6)
    for i in range(N):
        table[i].sort(key = lambda x: (-x[0], x[1]))
        max_value = max(max_value, table[i][0][0])
        min_number = min(min_number, table[i][0][1])
            
    # 최대 방문 방의 개수와 시작한 숫자 중 제일 작은 값
    print(f'#{tc} {min_number} {max_value}')


'''
9 3 4
6 1 5
7 8 2

3 4 5 (3,3)
4 5
6 7 8
7 8

1
3
9 4 3
7 5 2
8 2 6

[1,9] [1,4] []
[] [] []
[] [] []
: 존재하지 않았을테니까

[1,9] [2,4] []
[] [2,4] []
[] [] []
: 이제 넣어줄꺼

[1,9] [2,4] [1,3]
[] [2,4] []


2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2





'''