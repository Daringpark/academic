def lets_go(matrix):
    DP = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + matrix[i-1][j-1]
    # print(DP)
    return DP[N][M]

N, M = map(int, input().split())
Matrix = [list(map(int, input().split())) for _ in range(N)]
print(lets_go(Matrix))



'''
5 4
0 1 0 0
0 0 1 0
1 1 0 0
1 0 1 0
1 1 0 0
'''

'''
3 3
1 0 1
0 0 1
0 0 1
'''