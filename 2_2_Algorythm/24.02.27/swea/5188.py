import sys
sys.stdin = open("5188.txt")

def solve(x, y, s):
    global total_min_value
    if total_min_value <= s:
        return
    if x == N-1 and y == N-1:
        if total_min_value > s:
            total_min_value = s
        return
    if 0 <= x < N-1:
        solve(x+1, y, s+Matrix[x+1][y])
    if 0 <= y < N-1:
        solve(x, y+1, s+Matrix[x][y+1])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Matrix = [list(map(int, input().split())) for _ in range(N)]
    total_min_value = 1e10
    solve(0, 0, Matrix[0][0]) # 스타트 지점을 제외하고 합해주기 때문에 초기 값을 최소 값의 시작으로 받는다.
    print(f'#{tc} {total_min_value}')