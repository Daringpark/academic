import sys
sys.stdin = open('9386.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    space = list(map(int, input()))
    cnt = 0
    max_value = 0

    for i in range(N):
        if space[i] == 1 :
            cnt += 1
        else:
            cnt = 0
        if max_value < cnt:
            max_value = cnt
    print(f'#{tc} {max_value}')