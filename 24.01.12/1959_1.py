import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if n > m:
        A, B = B, A
        n, m = m, n
    # A와 B를 B와 A로, n과 m을 m과 n으로

    v = m-n+1
    D = []
    #회차별로 곱한 합을 최종 저장하는 집합

    for k in range(v):
        C = []
        #곱한 것을 저장하는 집합

        for j in range(n):
            x = A[j]*B[j+k]
            C.append(x)
        y = sum(C)
        D.append(y)
    ans = max(D)
    #최종 저장한 집합에서 max()함수를 통해 제일 큰 값을 빼냄

    #print(f'')를 통해서
    print(f'#{i} {ans}')