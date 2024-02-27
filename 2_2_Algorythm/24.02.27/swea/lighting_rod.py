# swea 전봇대
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rod_list = []
    for i in range(N):
        A, B = map(int, input().split())
        rod_list.append([A,B])
    cnt = 0
    for i in range(N):
        for j in range(N):
            if rod_list[i] != rod_list[j]:
                if rod_list[i][0] <= rod_list[j][0] and rod_list[i][1] >= rod_list[j][1]:
                    cnt += 1
    print(f'#{tc} {cnt}')