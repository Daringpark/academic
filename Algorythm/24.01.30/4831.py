import sys
sys.stdin = open('test.txt', 'r')

T = int(input()) # 노선 번호를 받는다 1<= T <= 50

for test_case in range(1, T+1):

    K, N, M = map(int, input().split())
    space = [0]*(N+K) # N개의 정류장 만들기
    lst = list(map(int, input().split()))

    pos = 0
    space[pos] = 1
    cnt = 0
    for number in lst :
        space[number] = 2 # 버스 정류장을 2로 봄
    space[]

    while pos < N : # 그라운드 범위를 벗어날 때, 조건을 완성하게 된다.
        print(pos, space)
        for i in range(K, 0, -1):
            if space[pos + i] == 2:
                space[pos] = 0
                pos += i
                space[pos] = 1
                cnt += 1
            elif space[pos+i] == 4:
                space[pos] = 0
                pos += 1
                space[pos] = 1
                cnt += 1
                break

    print(f'#{test_case} {cnt}')


