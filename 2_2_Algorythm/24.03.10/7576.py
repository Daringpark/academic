
## Tomato

import sys
input = sys.stdin.readline
from collections import deque
drdc = [[-1,0], [0,1], [1,0], [0,-1]]
M, N = map(int, input().split()) # N = row, M = col
Matrix = [list(map(int, input().split())) for _ in range(N)] # M,N 1000 한번 돌면 10**3**2 2천만 1초
days = [[-1] * M for _ in range(N)] # 값 뽑기
reaped = [] # 전체 익은 토마토 개수를 담아둠
for i in range(N):
    for j in range(M):
        if Matrix[i][j] == 1:
            reaped.append([i,j,0]) # 익어 있는 날짜는 day = 0
            days[i][j] = 0
        elif Matrix[i][j] == -1:
            days[i][j] = -2
queue = deque(reaped) 
max_value = 0

while queue: # BFS 탐색을 들어가자.
# 만약 익은 토마토가 없다라고 하면, 전부 못 익을 테니까 while문을 통과 할 수 없음
    item = queue.popleft() # 좌표가 들어가게 된다.
    row, col, day = item[0], item[1], item[2]
    if max_value < day:
        max_value = day
    # BFS할 수 있도록 해주자.
    for dr, dc in drdc:
        nr, nc = row + dr, col + dc
        if 0 <= nr < N and 0 <= nc < M and Matrix[nr][nc] == 0:
            Matrix[nr][nc] = 1 # 방문처리
            queue.append([nr,nc,day+1])
            days[nr][nc] = day+1
    # 우리는 days의 최대값을 뽑을 것이다.

# 갈 수 없는 공간이 존재할 때 all() any() method는 이럴때 편하다 하지만, 연산속도 ++
if any(-1 in row for row in days):    
    print(-1)
else:
    # 마지막에 나온 max_value가 최종 토마토가 익은 일의 날짜
    print(max_value)

# 0 시작이 여러 개일 경우, days 확인용
# for i in range(N):
    # print(*days[i])