'''
1
5
20 23
17 20
23 24
4 14
8 18
#1 4
'''


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    schedule = []
    for _ in range(N):
        schedule.append(list(map(int, input().split())))
    schedule.sort(key = lambda x: x[1]) # 끝나는 시간로 정렬하여서 쉽게 풀 수 있다.
    # 스케줄의 첫번째 값을 받아온다. 끝나는 시간을 기준으로 다음에 가져가야 할 스케줄의 시작과 비교하였을 때, end[1] <= start[2]

    # <while문 : 가현님>
    # idx = 0
    # cnt = 0
    # while idx < N: # 탈출한 idx는 N-1로 이 while문도 깔끔하게 탈출 가능
    #     end = schedule[idx][1]
    #     cnt += 1
    #     while idx < N and end > schedule[idx][0]: # idx == N-1에 도달하면 탈출하게 됨
    #         idx += 1

    # <내가 짰던 코드>
    # end = schedule[0][1]
    # idx = 1
    # cnt = 1
    # while idx < N-1: # N이랑 비교했을때, idx는 N-1까지 순회 할 예정; idx가 N이 되면 탈출하게 된다.
    #     while end > schedule[idx][0]: # 다음꺼 찾기 전까지 idx 올려주기
    #         idx += 1
    #         if idx == N:
    #             break
    #     if idx < N:
    #         cnt += 1
    #         end = schedule[idx][1]

    cnt = 1
    end = schedule[0][1]
    for i in range(1, N):
        if end <= schedule[i][0]:
            end = schedule[i][1]
            cnt += 1
    print(f'#{tc} {cnt}')