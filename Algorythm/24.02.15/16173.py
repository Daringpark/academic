import sys
sys.stdin = open('smail.txt')

# 외부로 나가는 경우, 즉사처리
# 출발점은 0,0 지점
# 이동방향을 아래 혹은 오른쪽
# N-1, N-1에 도달시 게임 즉시 종료
# 밟고 있는 칸만큼 움직여야한다.
N = int(input()) # N*N의 공간에서 쩰리는 점프한다.
space = [list(map(int, input().split())) for _ in range(N)]
print(space)

x, y = 0, 0 # start point
step = space[x][y]
while step != -1:
    dx, dy = [[step,0], [0,step]]
    for i in range(2):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N:
            x = new_x
            y = new_y
            step = space[x][y]
else: print(1)
