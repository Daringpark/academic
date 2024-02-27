import sys
sys.stdin = open("algo1_sample_in.txt")

def switch(A):
    if A:
        return 0
    else :
        return 1
def work_hard(i, j, number): # 2 2 1
    global space
    if number == 1: # i번째 부터 j개 뒤집기
        for y in range(j): # 2번째 돌부터 2개, 2,3 번째 (idx 1, 2번)
            if i-1+y < N:
                space[i - 1 + y] = switch(space[i-1+y])
    elif number == 2: # i번째 부터 j개의 돌을 i번째 돌과 같은 색깔로 바꾼다.
        for y in range(1, j):
            if i-1+y < N:
                if space[i-1] != space[i-1+y]: # 1이상으로 입력이 주어진다한다.
                    space[i-1+y] = space[i-1]
    elif number == 3: # i번째를 기준으로 j개 (양쪽으로 확인 j*2)
        for y in range(1, j+1):
            if 0 <= i-1-y < N and 0 <= i-1+y < N: # idx 자체가 우리가 의도한 것이랑 같은지 확인
                if space[i-1-y] == space[i-1+y]: # 조건에 맞으면 변환
                    space[i-1-y] = switch(space[i-1-y])
                    space[i-1+y] = switch(space[i-1+y])
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    space = list(map(int, input().split()))
    for _ in range(M):
        location, amount, work_number = map(int, input().split())
        work_hard(location, amount, work_number)
    res = ' '.join(map(str, space))
    print(f'#{tc} {res}')