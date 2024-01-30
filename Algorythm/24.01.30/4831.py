import sys
sys.stdin = open('test.txt', 'r')

T = int(input()) # 노선 번호를 받는다 1<= T <= 50

for test_case in range(1, T+1):

    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    
    pos = cnt = 0 # 현재 위치와 충전소 사용량을 초기화

    while pos + K < N : # 그라운드 범위를 벗어날 때, 조건을 완성하게 된다.
        for foot in range(K, 0, -1): #K, K-1, K-2, ... 1
            if (pos + foot) in stations:
                pos += foot
                cnt += 1
                print(pos, foot, cnt)
                break
        else :
            cnt = 0
            break
    print(f'#{test_case} {cnt}')


# 시뮬레이션처럼 그라운드를 만들고 싶었음.
space = [0]*N # N개의 정류장 만들기
space.extend([4]*K) # 정류장 범위 밖에 K만큼 추가
space[pos] = 1 # 출발 위치[0]; 현 위치를 1로 봄
for number in stations :
    space[number] = 2 # 충전소를 2로 봄
