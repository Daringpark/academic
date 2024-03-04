
def solve():
    # all 이라는 method를 활용할 수 도 있다. 슬라이싱보다 시간복잡도가 올라갈 수 도 있음

    # 가로 방향 확인하기
    for row in range(N):
        for col in range(N-4):
            if all(Matrix[row][col+i] == 'o' for i in range(5)):
                return 1
    # 세로 방향 확인하기
    for row in range(N-4):
        for col in range(N):
            if all(Matrix[row+i][col] == 'o' for i in range(5)):
                return 1
    # 대각선 방향 확인하기
    # row 탐색을 활용해서 아래로 내려가는 것만 확인하면 된다.
    # 우하향의 경우
    for row in range(N-4):
        for col in range(N-4):
            if all(Matrix[row+i][col+i] == 'o' for i in range(5)):
                return 1
    # 좌하향의 경우
    for row in range(N-4):
        for col in range(4,N): # Index내에서 확인할 수 있도록, 4에서 시작~ N-1까지
            if all(Matrix[row+i][col-i] == 'o' for i in range(5)):
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Matrix = [list(input()) for _ in range(N)]
    if solve():
        print(f'#{tc} YES')
    else: print(f'#{tc} NO')


### 이게 더 유동적으로 활용할 수 있음
dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]
def omok():
    for sr in range(n):
        for sc in range(n):
            if board[sr][sc] == 'o':
                for i in range(4):
                    row = sr
                    col = sc
                    cnt = 0
                    while 0 <= row < n and 0 <= col < n and board[row][col] == 'o':
                        cnt += 1
                        row += dr[i]
                        col += dc[i]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]

    print(f'#{tc} {omok()}')