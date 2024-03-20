
from collections import deque

def ready():
    global cnt
    
    while True: # 인구이동이 멈출때까지 계속...
        move_list = [] # 인구 이동할 것들 리스트
        moved = False
        visited = [[0] * N for _ in range(N)] # visited 처리를 통해서
        for i in range(N):
            for j in range(N):
                
                queue = deque()
                queue.append([i, j])
                visited[i][j] = 1
                
                temp = [] # 좌표 리스트
                temp_v = [] # 값 리스트
                while queue:
                    row, col = queue.popleft()
                    
                    for dr, dc in drdc:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < N and 0 <= new_col < N:
                            diff = abs(matrix[row][col]-matrix[new_row][new_col])
                            if L <= diff <= R: # 얘를 기준으로 인접한 것들을 다 모아
                                temp.append([new_row, new_col])
                                temp_v.append(matrix[new_row][new_col])
                                visited[new_row][new_col] = 1
                move_list.append([temp, temp_v])
        
        # 움직이자.
        for move in move_list:
            value = move[1]
    
    




# 시간 제한 2초 : 40,000,000


# 초기 세팅과 입력 받기
N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
drdc = [[-1,0], [0,1], [1,0], [0,-1]]
cnt = 0
ready()
        