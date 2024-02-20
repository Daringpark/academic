T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # start point 0 ~ N-M
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            per_sum = 0
            for k in range(M):
                for l in range(M): # 0, 1
                    per_sum += matrix[i+k][j+l]
            if max_sum < per_sum:
                max_sum = per_sum
    print(f'#{tc} {max_sum}')