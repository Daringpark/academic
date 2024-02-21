import sys
sys.stdin = open('16268.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    max_value = 0
    for row in range(N): # 행 우선 순회
        for col in range(M): # 열
            cnt = 0 # 각 위치에서 cnt를 초기화이후 셈
            cnt += matrix[row][col] # 현재 위치 +
            for k in range(4): # 상하좌우 +
                new_row = row + dr[k]
                new_col = col + dc[k]
                if 0 <= new_row < N and 0 <= new_col < M: # 바운더리 내 값만
                    cnt += matrix[new_row][new_col]
            if max_value < cnt: # 최대 꽃가루 개수 갱신
                max_value = cnt
    print(f'#{tc} {max_value}')