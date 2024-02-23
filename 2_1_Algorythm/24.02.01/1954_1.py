import sys
sys.stdin = open('1954_1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    space = [[0]*N for _ in range(N)]

    score = 0
    row = 0
    col = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    flag = 0

    for _ in range(N**2): # 값 채우기 for문
        score += 1
        new_row = row + dr[flag]
        new_col = col + dc[flag]

        space[row][col] = score #값 받기

        if new_row <0 or new_col <0 or new_row >= N or new_col >= N or space[new_row][new_col]:
            flag = (flag+1)%4 # 바운더리 넘지 않기, 값이 있으면, 방향 전환

        row += dr[flag]
        col += dc[flag]
    print(f'#{tc}')
    for row in range(N):
        for col in range(N):
            print(space[row][col], end = ' ')
        print()
