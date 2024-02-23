import sys
sys.stdin = open('9490.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    total_max = 0
    for row in range(N):
        for col in range(M): # 하나씩 움직이면서
            max_value_pos = matrix[row][col]
            length = matrix[row][col]
            for i in range(4): # 상하좌우 조작
                for l in range(1, length+1): # 길이만큼 전진하며 계속 더하기
                    new_row = row + dr[i]*l
                    new_col = col + dc[i]*l
                    if 0 <= new_row < N and 0 <= new_col < M:
                        max_value_pos += matrix[new_row][new_col]
                    if total_max < max_value_pos:
                        total_max = max_value_pos
    print(f'#{tc} {total_max}')


