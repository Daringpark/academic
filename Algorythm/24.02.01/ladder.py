import sys
sys.stdin = open('input_ladder.txt', 'r')

for tc in range(10):
    space = []
    N = int(input())
    for n in range(100): # 데이터 불러오기
        matrix = list(map(int, input().split()))
        space.append(matrix)

    # pos = space[99][X]
    # 기본 matrix setting
    row = 99
    col = 0
    for i in range(100): # 찾았다. 몇 번째 열인지
        found = space[99][i]
        if found == 2:
            col = i
    dr = [-1, 0, 0] #위 좌 우
    dc = [0, -1, 1]
    flag = 0
    new_row = row + dr[flag]
    new_col = col + dc[flag]

    for i in range(100):
        # 좌우 살피기
        if space[row][col-1] == 1: # 좌측이 1일때, 0이 나올때까지 직진
            flag = 1
            while space[new_row][new_col] != 0:
                col += dc[flag]
            flag = 0
        
        elif space[row][col+1] == 1: # 우측이 1일때, 0이 나올때까지 직진
            flag = 2
            while space[new_row][new_col] != 0:
                col += dc[flag]
            flag = 0
        # # 바운더리 밖에 있는지, 파악할 필요가 없음.
        # if new_row < 0 or new_col < 0 or new_row >= N or new_col >= N :
    row += dr[flag]
    col += dc[flag]
    ans = col

    print(f'#{N} {ans}')


