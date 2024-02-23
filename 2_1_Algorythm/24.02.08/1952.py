M, N = map(int, input().split())


space = [[0] * N for _ in range(M)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]
flag = 0
cnt = 0
for row in range(M):
    for col in range(N):
        if 0 <= row < M and 0 <= col < N and space[row][col] == 0:
            space[row][col] = 1
        else:           
            if flag == 3:
                flag = 0
            flag += 1
            cnt += 1
        new_row = row + dr[flag]
        new_col = col + dc[flag]

print(space, cnt)