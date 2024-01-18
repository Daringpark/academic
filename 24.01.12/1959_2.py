import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    v = m-n+1
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    D = []

    if n >= m :
        A, B = B, A

    for k in range(v):
        for j in range(n):
            x = A[j]*B[j+k]
            C.append(x)
        y = sum(C)
        D.append(y)
    ans = max(D)
    print(f'#{i} {ans}')