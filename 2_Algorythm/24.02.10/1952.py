M, N = map(int, input().split())
space = [[0]*N for _ in range(M)]
row = col = 0
dr = [0,1,0,-1]
dc = [1,0,-1,0]
flag = 0
end = N*M-1
cnt = turn = 0
space[0][0] = 1
while turn != end: # turn이 총 길이까지 갈 때, 멈추게 된다.
    new_row = row + dr[flag]
    new_col = col + dc[flag]
    if 0 <= new_row < M and 0 <= new_col < N and space[new_row][new_col] == 0:
        space[new_row][new_col] = 1
        row = new_row
        col = new_col
    else:
        cnt += 1
        flag += 1
        turn -= 1
    turn += 1
    if flag == 4:
        flag = 0
print(cnt)