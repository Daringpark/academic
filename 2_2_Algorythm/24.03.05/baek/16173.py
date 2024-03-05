import sys
sys.stdin = open('smail.txt')

# 외부로 나가는 경우, 즉사처리
# 출발점은 0,0 지점
# 이동방향을 아래 혹은 오른쪽
# N-1, N-1에 도달시 게임 즉시 종료
# 밟고 있는 칸만큼 움직여야한다.
N = int(input()) # N*N의 공간에서 쩰리는 점프한다.
space = [list(map(int, input().split())) for _ in range(N)]
stack = []
stack.append([0, 0])
step = space[0][0]
while stack and step >= 0:
    item = stack.pop()
    step = space[item[0]][item[1]]
    for j in range(2):
        if j:
            new_row = item[0] + step
            new_col = item[1]
        else:
            new_row = item[0]
            new_col = item[1] + step
        if 0 <= new_row < N and 0 <= new_col < N and step != 0:
            stack.append([new_row, new_col])
    if step == -1:
        print("HaruHaru")
        break
if step != -1:
    print("Hing")