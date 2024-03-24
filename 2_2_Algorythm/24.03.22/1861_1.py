def dfs(row, col):
 
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newR = row+dr
        newC = col+dc
        if 0<=newR<N and 0<=newC<N and matrix[newR][newC] == matrix[row][col]+1:
            if visited[newR][newC] == 0:
                visited[newR][newC] = dfs(newR, newC)
            return visited[newR][newC] + 1
 
    return 1
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
 
    maxV = 0 # 맥스 값 조정
    roomno = N*N # 최대로 나올 수 있는 룸 넘버
    
    visited = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 0:
                visited[row][col] = dfs(row, col)
                if visited[row][col] > maxV:
                    maxV = visited[row][col]
                    roomno = matrix[row][col]
                elif visited[row][col] == maxV:
                    roomno = min(roomno, matrix[row][col])
    print(f'#{tc} {roomno} {maxV}')