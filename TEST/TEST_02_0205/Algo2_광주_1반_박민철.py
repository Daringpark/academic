# import sys
# sys.stdin = open('algo2_sample_in.txt', 'r')
# 테스트 케이스 확인용
#################################################
T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())
    space = list(map(int, input().split()))

    pos = 0 # 현재 위치
    flag = 0 # 뒤로 갔는지 판단
    pre = 0 # 후진했을 때, 이전 위치값을 저장
    score = 0 # 최종 결과
    for _ in range(K):
        if pre < 0: # 이전 위치의 값이 음수였다면, 후진한 것으로 판단
            flag = 1
        pre = space[pos] # 지금 시점에서 저장
        pos += space[pos] # 지금 위치에서 전진
        if flag == 1:
            pos -= space[pre]
            flag = 0
        if 0 <= pos < N: # pos가 범위 안에 있을 경우
            score += space[pos]
        else :
            break

    print(f'#{tc} {score}')