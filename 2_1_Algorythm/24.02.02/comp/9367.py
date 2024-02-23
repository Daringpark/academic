import sys
sys.stdin = open('9367.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     space = list(map(int, input().split())) + [0]
#     # 마지막 열까지 비교할 수 있도록 조작해준다
#     max_cnt = 1 # 최종 출력값
#     cnt = 1 # 초기 길이
#     for i in range(N): # 마지막 전까지 처음과 다음걸 비교
#         if space[i] < space[i+1]: # 다음 것이 더 크면, 카운트
#             cnt += 1
#         else:
#             if cnt > 1 and max_cnt < cnt:
#                 max_cnt = cnt
#                 cnt = 1
#
#     print(f'#{tc} {max_cnt}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    space = list(map(int, input().split()))
    max_cnt = 1 # 최종 출력값
    cnt = 1 # 초기 길이
    for i in range(N-1): # 마지막 전까지 처음과 다음걸 비교
        if space[i] < space[i+1]: # 다음 것이 더 크면, 카운트
            cnt += 1
        else: # 마지막 전까지 다음 것과 비교하지만, 앞이 더 클 경우
            cnt = 1
        if cnt > 1 and max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')
