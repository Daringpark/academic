
def row_check():

    for row in range(N):
        visited = [0] * N
        # 왼쪽 -> 오른쪽 내려간다
        for col in range(N-1):
            if matrix[row][col] == matrix[row][col+1] + 1:

        


        # 오른쪽 -> 왼쪽 내려간다
        for col in range(N, 0, -1):
            if matrix[row][col] == matrix







N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]









# 경사로를 확인할 때 양쪽을 확인해야한다.
visited = [0] * N

result = 0




