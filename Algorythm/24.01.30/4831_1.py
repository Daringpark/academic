# 민규 풀이
import sys
sys.stdin = open('test.txt', 'r')

T = int(input())
 
for t in range(T):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
 
    # 한 번에 K 만큼 이동할 수 있음
    # N 까지 가고싶음
    # M 개만큼 충전소 있음
 
    # 마지막 충전한 충전소의 K 범위 이내에 있는 것이 끝까지 반복되면 됨
    chargers = [0] * (N + 1)
    for m in stops:
        chargers[m] = 1
 
    # 0부터 이동해보자
    count = 0
    available = True # moveable
    i = 0
    while i + K < N:
        drive_range = chargers[i + 1:i + (K + 1)]
        if 1 in drive_range:
            # 가장 멀리 있는 충전소 좌표 따기
            r_drive_range = list(reversed(drive_range))
            far_temp = r_drive_range.index(1)
            far = K - far_temp
            i = i + far
            count += 1
        else:
            available = False # moveable
            break
 
    if available:
        print(f"#{t + 1} {count}")
    else:
        print(f"#{t + 1} 0")