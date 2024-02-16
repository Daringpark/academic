def bfs(s): # 너비 우선 탐색하겠다.
    Q = [] # 빈 Queue를 생성
    visited = [0] * (N+1) # 내가 지나갔던 지점을 기억하기

    Q.append((s, 1)) # 스타트 지점을 Queue에 추가하기
    visited[s] = True # 지났던 지점을 기억하는 리스트의 스타트 지점 index를 True
    while Q:
        v, d = Q.pop(0) #
        print(v, d)

        for w in range(N+1): # 옆으로 확인할 것입니다.
            if G[v][w]==1 and not visited[w]: # 그래프의 v, w가 1이면서 방문하지 않았다면
                Q.append((w, d+1)) # Queue에 추가
                visited[w] = True # 지금의 visited를 추가해준다.


N, E = map(int, input().split())
lst = list(map(int, input().split()))

# G = [[] for _ in range(N+1)]
'''
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
'''
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(0, len(lst), 2):
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1][v2] = 1
    G[v2][v1] = 1

# print(G)
bfs(1)
