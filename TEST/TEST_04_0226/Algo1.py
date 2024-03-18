def calculate():
    value = matrix[row][col] # 터트린 위치의 값을 받음
    for i in range(4): # 시계방향으로 사거리만큼 순회
        for k in range(1,3): # 상하좌우의 사거리 1, 사거리 2를 반복문을 돌면서 간다.
            new_row = row + k*drdc[i][0]
            new_col = col + k*drdc[i][1]
            if 0 <= new_row < N and 0 <= new_col < N:
                value += matrix[new_row][new_col]
    return value
T = int(input()) # 테스트 케이스
for tc in range(1, T+1):

    N = int(input()) # N*N matrix
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # Matrix 불러오기
    drdc = [(-1,0), (0,1), (1,0), (0,-1)] # 시계방향을 돌아간다.
    max_value = 0
    for row in range(N): # 행, 열 순회할 수 있도록
        for col in range(N):
            if max_value < calculate(): # 계산된 값과 max_value를 비교하여 최대값 갱신
                max_value = calculate()
    print(f'#{tc} {max_value}')