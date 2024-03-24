'''
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2

1
3
9 3 4
6 1 5
7 8 2

1
3
9 4 3
7 5 2
8 2 6
'''

import sys
sys.stdin = open("1861_input.txt")
sys.stdout = open("1861_output.txt", "w")
from collections import deque
# 서로 다른 수 << 조건이 있음
def bfs(start):
    global min_number, max_value
    # 첫 시작을 잡아서 탐색 돌기
    # 초기 세팅
    q = deque([start])
    start_r, start_c = start
    if not visited[start_r][start_c]:
        visited[start_r][start_c] = 1
    
    # BFS를 하고 나왔을 때, 나온 면적과 최소값을 글로벌과 비교
    while q:
        row, col = q.popleft()
        
        for dr,dc in drdc: # 탐색을 하고자 한다.
            new_r = row + dr
            new_c = col + dc
            
            if 0 <= new_r < N and 0 <= new_c < N: # 일단 범위 내에 있는지부터 판단한다
                # 조건에 부합하는지 판단한다
                if matrix[row][col] + 1 == matrix[new_r][new_c]:
                    
                    # 지금의 visited + 1이랑 내딛을 visited랑 비교해서 지금의 visited가 더 크면, 교체해준다.
                    if visited[row][col] + 1 > visited[new_r][new_c]:
                        visited[new_r][new_c] = visited[row][col] + 1
                        q.append([new_r, new_c])
                        
    # 마지막에 뽑았던 row,col이 결국 visited에 최대 크기를 품고 있는 행열이다.
    # 그럼 그들 사이에서 최소는 어떻게 구해야 하는가?
    if max_value < visited[row][col]:
        max_value = visited[row][col]
        min_number = matrix[start_r][start_c]
    # elif가 필수적
    elif max_value == visited[row][col] and min_number > matrix[start_r][start_c]:
        min_number = matrix[start_r][start_c]
    
drdc = [[-1,0], [0,1], [1,0], [0,-1]]
T = int(input())
for tc in range(1, T+1):
    
    N = int(input()) # N = 1e3
    # 1e6 matrix
    # 값도 1e6,  1e12
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # visited에는 최대 방문한 방 개수와 최소 시작 숫자를 넣기
    visited = [[0] * N for _ in range(N)]
    max_value = 0
    min_number = int(1e6)
    
    for i in range(N):
        for j in range(N):# 1e12
            bfs([i,j]) # 완탐을 돌면서 갱신
    
    # 최대 방문 방의 개수와 시작한 숫자 중 제일 작은 값
    print(f'#{tc} {min_number} {max_value}')
