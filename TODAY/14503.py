# 14503 로봇 청소기


'''
N * M
# 0 0 (row, col) 제일 위 왼
# N-1, M-1 (row, col) 제일 아래 오

각 칸은 벽과 칸으로 이뤄져 있다.
청소기가 바라보는 방향이 존재하다.

1. 현재 칸이 청소 되지 않은 경우, 청소를 한다.

2. 현재 칸의 주변 4칸이 청소 되지 않은 빈칸이 없는 경우 (청소가 다 되어있는경우)
- 바라보는 방향을 유지하고, 후진 가능하다면 후진하여 1.
- 바라보는 방향의 뒤쪽 칸이 벽이라서 후진하지 못한다면, 작동 중지

3. 현재 칸의 주변 4칸이 청소되지 않은 빈칸이 있는 경우 (청소가 필요한 칸이 있는 경우)
- 반 시계로 90도 회전한다.
- 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 칸이면 한 칸 전진하고 1.
'''
drdc = [[-1,0], [0,1], [1,0], [0,-1]]
# 후진 하는 경우 direction + 2 % 4


def simulate():
    global Matrix
    cnt = 0
    row, col = startrow, startcol
    direction = startdir

    # 일단, 현재 칸을 청소하자.
    Matrix[row][col] = 1
    cnt += 1
    flag = 0

    # 그리고 탐색부터 하자.
    for i in range(4):
        new_row = row + drdc[i][0]
        new_col = row + drdc[i][1]
        if Matrix[new_row][new_col] == 0:
            flag = 1  # 청소 위치 확인하였다.
            break
    
    
    while not Matrix[row+drdc[direction][0]][col+drdc[direction][1]]:
        # False인 경우 (보는 방향에 먼지가 있는 경우), True
        
        
        
        
        direction = (direction+1) % 4 # 90도 시계방향 회전한다.
    

    # new_row = row + drdc[direction]
    # new_col = col + drdc[direction]






    return cnt


N, M = map(int, input().split()) # matrix 전개
startrow, startcol, startdir = map(int, input().split()) # 시작 위치 + 보고 있는 방향
# 0 1 2 3 북 동 남 서 (반 시계 방향)
Matrix = [list(map(int, input().split())) for _ in range(N)]
# 0인 경우 무조건 청소되지 않은 칸이다.
# 1인 경우는 벽이다.
# 내가 지나갔던 1번을 다시 갈 필요가 없는가?

print(simulate())