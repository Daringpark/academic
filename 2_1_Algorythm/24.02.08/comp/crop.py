import sys
sys.stdin = open('crop.txt')

def f(n):
    if n > 2 :
        for i in range(3, n+1):
            memo[i] = memo[i-1] + 2 * memo[i-2]
    return memo[n]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N //= 10
    memo = [0 for i in range(N+1)]
    memo[1] = 1
    memo[2] = 3
    print(f'#{tc} {f(N)}')