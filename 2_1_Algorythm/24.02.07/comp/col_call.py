import sys
sys.stdin = open('col_call.txt')

T = int(input())

for tc in range(1, T+1):
    space = [list(input()) for _ in range(5)]

    N = max(len(space[i]) for i in range(5))
    res = ''
    for i in range(N):
        for j in range(5):
            try: res += space[j][i]
            except IndexError: pass

    print(f'#{tc} {res}')