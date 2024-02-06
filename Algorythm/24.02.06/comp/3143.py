import sys
sys.stdin = open('input_3143.txt')

# T = int(input())
# for tc in range(1, T+1):
#     A, B = map(str, input().split())
#     # 내장함수?
#     N = len(A)
#     M = len(B)
#     cnt = N + (-M+1)*A.count(B)
#     print(f'#{tc} {cnt}')

# A의 길이는 10000 이하, B의 길이는 100이하
# Brute force # list로 풀기 싫은데

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    N = len(A)
    M = len(B)

    cnt = 0
    pos = 0

    while pos < N: # N-1까지 순회
        if pos <= N-M and A[pos:pos+M] == B: # N-M이 while 안으로 들어가야함
            cnt += 1
            pos += M
        else :
            cnt += 1
            pos += 1
    print(f'#{tc} {cnt}')