import sys
sys.stdin = open('6485.txt', 'r')

T = int(input()) # testcase number

for tc in range(1, T+1):
    N = int(input()) # bus number

    bus = []
    for i in range(N):
        bus.append(list(map(int, input().split()))) # 정류장 범위 받기

    # brute force
    P = int(input()) # 버스 정류장 개수 받기
    number = []
    for j in range(P):
        busstop = int(input()) # 지금 버스 정류장에 대입하기
        cnt = 0
        for k in range(N):
            A, B = bus[k][0], bus[k][1]
            if A <= busstop <= B:
                    cnt += 1
        number.append(cnt)

    print(f'#{tc}', end = ' ')
    for i in range(P):
        print(number[i], end = ' ')
    print()

# busstop이 중복이 없다고 하면, dictionary화 시킬 수도 있음.
# key = busstop number, value = count