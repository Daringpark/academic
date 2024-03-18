

M, N, K = map(int, input().split())

# 왼쪽 아래가 0,0 오른쪽 위가 N,M (M-M, N-N)
# 0 , 2 >> M - (M-0), N - (N-2) 
# 2 5 >> M 5 - 2, N 7 - 5


matrix = [[0] * N for _ in range(M)]
for i in range(M):
    print(*matrix[i])

# 0,0 1,1 > 1칸 (1,5) 칸까지가 영역으로 쓰일 수 있음