import sys
sys.stdin = open('input_ladder.txt', 'r')

# matrix 내에서 움직일 수 있도록, Index Error가 나지 않도록 가이드 라인
def boundary(a, b):
    if 0<= a < 100 and 0<= b < 100:
        return True
    else:
        return False

for tc in range(10):
    space = []
    N = int(input())
    for n in range(100): # 데이터 불러오기
        matrix = list(map(int, input().split()))
        space.append(matrix)

    # pos = space[99][X]
    # 기본 matrix setting
    for i in range(100): # 찾았다. 몇 번째 열인지
        if space[99][i] == 2:
            X = i
            break
    row = 99
    col = X
    dr = [-1, 0, 0] #위 좌 우
    dc = [0, -1, 1]
    flag = 0

    while row > 0: # 0번째 행에 도착할 경우 while문에서 빠져나옴
        if flag == 0: #위를 보면서 좌우 살피기
            # 좌측 보기
            if boundary(row, col + dc[1]) and space[row][col+dc[1]] == 1:
                flag = 1
                row, col = row + dr[flag], col + dc[flag]
            elif boundary(row, col + dc[2]) and space[row][col+dc[2]] == 1:
                flag = 2
                row, col = row + dr[flag], col + dc[flag]
            else:
                row, col = row + dr[flag], col + dc[flag]

        else: # 좌우를 보고 있는 상황, 막혀 있다면 다시 위로
            if space[row+dr[0]][col] == 1: # 위로 올라가기
                flag = 0
                row, col = row + dr[flag], col + dc[flag]
            else : # 좌 우 방향으로 쭉 가기
                row, col = row + dr[flag], col + dc[flag]

    print(f'#{N} {col}')