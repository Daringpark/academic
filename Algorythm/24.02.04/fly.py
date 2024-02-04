
T = int(input())
for tc in range(1, T+1):

    D, A, B, F = map(int, input().split())
    Time = D/(A+B) # 시간은 거리/상대속도
    distance = Time * F

    print(f'#{tc} {distance}')