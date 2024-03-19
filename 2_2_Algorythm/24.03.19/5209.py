def make_min(n, s):
    global result
    
    # 합이 이미 넘어버렸을때
    if result and s > result:
        return
    
    # 레벨링을 마쳤을때
    if n == N:
        if not result: #초기 result 값을 어케 정할 것?
            result = s
        result = min(result, s)
        return
    
    # 재귀 돌기
    for i in range(N):
        if not visited[i]: # visited 판별로 permutation 구하기
            visited[i] = 1
            make_min(n+1, s+matrix[n][i]) #
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0 # 값 출력
    make_min(0, 0) # leveling
    
    print(f'#{tc} {result}')