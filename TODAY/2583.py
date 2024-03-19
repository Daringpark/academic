

M, N, K = map(int, input().split())

# 왼쪽 아래가 0,0 오른쪽 위가 N,M (M-M, N-N)
# 0 , 2 >> M - (M-0), N - (N-2) 
# 2 5 >> M 5 - 2, N 7 - 5
# M*N = 10**4*K(10**2) = 1e6


matrix = [[0] * N for _ in range(M)]
for i in range(M):
    print(*matrix[i])

# 0,0 1,1 > 1칸 (1,5) 칸까지가 영역으로 쓰일 수 있음
# 0,0 1,1 > M-1 row, 0 (1-1) col
# 0,2 4,4
# 1,1 2,5
# 4,0 6,2

for k in range(K):
    start_x, start_y, end_x, end_y = map(int, input().split())