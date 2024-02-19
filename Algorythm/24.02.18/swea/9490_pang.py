

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    drdc = [[-1,0], [0,1], [1,0], [0,-1]] # 상하좌우로
    max_sum = 0
    for row in range(N):
        for col in range(M):
            per_sum = matrix[row][col]
            power = matrix[row][col]
            for i in range(4):
                for k in range(1, power+1):
                    new_row = row + k*drdc[i][0]
                    new_col = col + k*drdc[i][1]
                    if 0 <= new_row < N and 0 <= new_col < M:
                        per_sum += matrix[new_row][new_col]
            if max_sum < per_sum:
                max_sum = per_sum
    
    print(f'#{tc} { max_sum}')