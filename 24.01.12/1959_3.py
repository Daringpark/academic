import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    m, n = map(int, input().split())
    o = 0
    p = 0
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if m > n: #5개랑 3개
        J, I = A, B
        p, o = n, m
    else :
        I, J = A, B
        o, p = n, m

    v = m - n + 1
    I = []
    J = []
    C = []
    D = []

    for j in range(v):
        for k in range(p):
            x = A[k]*B[k+j]
            C.append(x)
        y = sum(C)
        D.append(y)
        print(D)
    ans = max(D)
    print(f'#{i} {ans}')