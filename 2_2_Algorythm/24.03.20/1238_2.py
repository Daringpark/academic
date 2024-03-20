# 성은이 풀이

from collections import deque
 
def bfs(s):
    Q = deque()
    Q.append(s)
    visited[s] = 1
    while Q: # Q가 빌 때까지 반복
        d = Q.popleft()
        for a in G_lst[d]:
            if visited[a] == 0: # 아직 방문을 안 했다면
                Q.append(a)
                visited[a] = visited[d] + 1
 
T = 10
 
for tc in range(T):
    N, s = map(int, input().split()) # 데이터의 길이, 시작 번호
    G = list(map(int, input().split()))
    G_lst = [[] for _ in range(101)]
    for i in range(N//2):
        G_lst[G[2*i]].append(G[2*i+1])
 
    visited = [0] * 101  # 방문표시
    bfs(s)
    maxV = max(visited) # 가장 늦게 연락 받은 사람들이 얼마나 늦게 받았는지
    visited.reverse() # 숫자가 가장 큰 사람(reverse전 기준 visited에서 가장 오른쪽에 있는 사람)을 찾기 위해
 
    print(f'#{tc+1} {100-visited.index(maxV)}')
