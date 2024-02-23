import sys
sys.stdin = open('4836.txt', 'r')

def find():
    cnt = 0
    for i in range(10):
        for j in range(10):
            if space[i][j] == 3:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    space = [[0 for i in range(10)] for j in range(10)] # 도화지 생성
    N = int(input())
    for order in range(N): # N번 칠해주겠다.
        r1, c1, r2, c2, c = map(int, input().split()) #시작점과 끝점, 색깔
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if space[i][j] == 0:
                    space[i][j] = c
                elif c == 1 and space[i][j] == 2:
                    space[i][j] = 3
                elif c == 2 and space[i][j] == 1:
                    space[i][j] = 3

    print(f'#{tc} {find()}')
