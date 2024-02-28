
import sys
sys.stdin = open("bread.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    COUNTS = [0] * (max(customers)//M+1)
    for i in range(M, max(customers)+1):
        if not COUNTS[i//M]:
            COUNTS[i//M] = K
    print(COUNTS)
    for customer in customers: # 직접 순회하면서 빼기
        COUNTS[customer//M] -= 1
    if -1 in COUNTS:
        print(f'#{tc} Impossible')
    else: print(f'#{tc} Possible')