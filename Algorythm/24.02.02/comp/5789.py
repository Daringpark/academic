import sys
sys.stdin = open('5789.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    bucket = [0]*N
    for i in range(1, Q+1):
        s, e = map(int, input().split())
        for paint in range(s-1, e):
            bucket[paint] = i

    print(f'#{tc}', end= ' ')
    for i in range(N):
        print(f'{bucket[i]}', end = ' ')
    print()
