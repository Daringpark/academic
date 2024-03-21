import sys
sys.stdin = open("5250.txt")

from collections import deque
def path_find():
    
    min_value = int(1e6)
    # BFS or dijkstra or DP
    D = [[(min_value)] * N for _ in range(N)]
    D[0][0] = 0 # 시작지점
    q = deque([[0,0]])
    while q:
        row, col = q.popleft()
        for dr, dc in [[-1,0], [0,1], [1,0], [0,-1]]:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < N and 0 <= new_col < N:
                diff = matrix[new_row][new_col] - matrix[row][col] + 1
                if 1 < diff:
                    W = diff
                else: W = 1
                # W = max(1, matrix[new_row][new_col]-matrix[row][col]+1) # 가야할 곳이 더 높을 때가 중요함
                if D[new_row][new_col] > D[row][col] + W:
                    D[new_row][new_col] = D[row][col] + W
                    q.append([new_row, new_col])

    # return D[e[0]][e[1]] # 마지막에 제일 좋은 값이 들어가 있을 것이다.
    return D[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    
    N = int(input()) # 1e2
    matrix = [list(map(int, input().split())) for _ in range(N)] # 값은 1e3
    # print(matrix)
    # start = 0, 0
    # end = N-1, N-1
    # start = [0,0]
    # end = [N-1,N-1]

    print(f'#{tc} {path_find()}')