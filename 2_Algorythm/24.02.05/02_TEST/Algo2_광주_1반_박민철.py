import sys
sys.stdin = open('algo2_sample_in.txt', 'r')
# 테스트 케이스 확인용
#################################################
T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())
    space = list(map(int, input().split()))

    pos = 0 # 현재 위치
    pre = 0 # 이전 위치 값
    score = 0 # 최종 결과 값
    flag = 0 # 후진 판별

    for _ in range(K):
        if space[pos] < 0: # 값이 음수인 경우, 이전 위치 저장
            pre = space[pos]
            flag = 1
        if flag and space[pos] > 0: # flag와 양수 값이 나올 경우, 추가 이동
            pos += space[pos] - pre
            flag = 0 # flag 초기화
        else : # flag가 꺼진 경우, 일반 이동 (전진, 후진)
            pos += space[pos]
        if 0 <= pos < N: # 범위 안에서 이동하기
            score += space[pos]
        else :
            break # 범위 밖 조기 종료

    print(f'#{tc} {score}')