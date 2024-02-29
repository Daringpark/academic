
T = int(input().strip())
tower = {'A' : 1, 'B' : 2, 'C' : 3, 'X': 0, 'H': 0}
for tc in range(1, T+1):

    N = int(input().strip())
    Matrix = [list(input().strip()) for _ in range(N+1)] # 0 ~ N (N+1개)
    drdc = [[-1,0], [0,1], [1,0], [0,-1]]
    cnt = 0
    for row in range(N):
        for col in range(N):
            if Matrix[row][col] == 'H':
                flag = 1
                for k in drdc:
                    for idx in range(1,4): # 범위 1~3
                        new_row = row + k[0]*idx
                        new_col = col + k[1]*idx
                        # 카운팅에서 문제가 생기는 중..
                        if 0 <= new_row < N and 0 <= new_col < N: # 범위 안에 들어가게
                            if idx <= tower[Matrix[new_row][new_col]]: # 1,2,3 XH 0 ABC 1 2 3
                                flag = 0 # 기지 발견
                                break
                if flag: # 1 기지발견 못함
                    cnt += 1
                # print(row, col, flag, cnt)
    print(f'#{tc} {cnt}')
    for i in range(N):
        print(*Matrix[i])

'''
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
XXXXXXXXX
'''