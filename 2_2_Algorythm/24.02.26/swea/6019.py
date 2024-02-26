'''
1
250 10 15 20
'''
T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    res = F * D/(A+B)
    print(f'#{tc} {res}')