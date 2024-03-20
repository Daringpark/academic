# 가현이 풀이
from collections import deque
 
def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
 
    while q:
        v = q.popleft()
 
        for next in G[v]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[v] + 1
 
 
T =10
for tc in range(T):
    l,s = map(int, input().split())
    arr = list(map(int ,input().split()))
    G = [[] for _ in range(101)]
    for idx in range(0,l-1,2):
        if arr[idx+1] not in G[arr[idx]]:
            G[arr[idx]].append(arr[idx+1])
    # print(G)
    visited = [0] * 101
    bfs(s)
    # print(visited)
    last = max(visited)
    lst = []
    for idx in range(101):
        if visited[idx] == last:
            lst.append(idx)
    print(f'#{tc+1} {max(lst)}')