

direction = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    Matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_value = 0
    for row in range(N):
        for col in range(M):
            cnt = 0
            for i in range(8):
                new_row = row + direction[i][0]
                new_col = col + direction[i][1]
                if 0 <= new_row < N and 0 <= new_col < M and Matrix[new_row][new_col] < Matrix[row][col]:
                    cnt += 1
                if cnt >= 4:
                    sum_value += 1
                    break
    print(f'#{tc} {sum_value}')
'''
4
3 5
2 3 1 8 9 
7 6 2 2 6 
5 7 3 8 7 
5 5
5 2 3 5 2 
5 5 8 4 5 
3 6 8 5 2 
8 2 3 3 3 
5 1 5 4 5 
5 8
8 7 2 5 2 4 3 1 
7 4 2 3 9 3 5 1 
5 7 6 2 2 7 9 6 
9 8 7 6 2 1 9 4 
1 9 4 9 2 3 5 2 
10 5
6 1 2 3 3 
5 2 4 6 9 
2 3 8 4 5 
4 9 7 4 3 
2 8 5 9 7 
6 1 8 7 4 
1 4 5 8 6 
5 6 2 8 5 
4 2 9 8 2 
1 9 9 6 9 
'''