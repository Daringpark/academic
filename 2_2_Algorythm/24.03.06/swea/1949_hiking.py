import sys
from collections import deque


drdc = [[-1,0], [0,1], [1,0], [0,-1]]


def check_max(matrix):
    max_value = 0
    for i in range(N):
        for j in range(N):
            if max_value < matrix[i][j]:
                max_value = matrix[i][j]
    
    max_list = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_value:
                max_list.append([i, j])
    return max_list
def check_route(highest_list, matrix):
    
    max_value = 0
    for highest in highest_list: # 산 peak max 5 
        # 피크 지점에서 시작하는데, 그 방향에서 가는게 아니라
        # 전체 visited를 지금 관리하고 있다.
        # 오류를 없애자.
        # 거기에서 또 나아갈 방향을 가져와야함.

        peak_to_under = []
        for i in range(4): # direciton
            new_row = highest[0] + drdc[i][0]
            new_col = highest[1] + drdc[i][1]
            if 0 <= new_row < N and 0 <= new_col < N:
                peak_to_under.append([new_row, new_col])
        
        for start in peak_to_under:
            queue = []
            visited = [[0] * N for _ in range(N)]
            visited[start[0]][start[1]] = 2 # visited checked
            queue.append([start[0], start[1]])
            while queue:
                item = queue.pop(0)
                for i in range(4): # direciton
                    row = item[0] + drdc[i][0]
                    col = item[1] + drdc[i][1]
                    if 0 <= row < N and 0 <= col < N: # in boundary
                        if not visited[row][col]:
                            if matrix[item[0]][item[1]] > matrix[row][col]:
                                visited[row][col] = visited[item[0]][item[1]] + 1
                                queue.append([row, col])
                            elif matrix[item[0]][item[1]] - K > matrix[row][col]:
                                visited[row][col] = visited[item[0]][item[1]] + 1
                                queue.append([row, col])
                        if max_value < visited[row][col]:
                            max_value = visited[row][col]
    return max_value


T = int(input())
for tc in range(1, T+1):
    
    N, K = map(int, input().split())
    Matrix = [list(map(int, input().split())) for _ in range(N)]
    # check_route(check_max(Matrix), Matrix)
    print(f'#{tc} {check_route(check_max(Matrix), Matrix)}')

'''
1   
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8

1
3 2       
1 2 1     
2 1 2
1 2 1

'''