def f(i, k, s):
    global min_V
    if i == k: # 최종 노드로 도달하기까지
        # print(*P) # 원소 출력
        if min_V > s:
            min_V = s
    elif s >= min_V: # 최소값보다 크면 의미가 없음; node 위로 올라가기
        return
    else: # 노드 아래로 순회
        for j in range(i, k): # P[i] <-> P[j]
            P[i], P[j] = P[j], P[i] # 교환하기
            f(i+1, k, s+space[i][P[i]]) # Back-tracking
            P[i], P[j] = P[j], P[i] # 복구하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [i for i in range(N)]
    min_V = 10**10
    space = [list(map(int, input().split())) for _ in range(N)]
    f(0, N, 0)
    print(f'#{tc} {min_V}')