'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e) # 양 방향으로
    graph[e].append(s)

def dfs(V):
    stack = [V]
    visited = []
    while stack:
        item = stack.pop()
        if item not in visited:
            visited.append(item)
            stack.extend(sorted(graph[item], reverse=True)) # 역순 탐색 (작은게 stack의 끝에 가도록)
    print(*visited)

def bfs(V):
    queue = deque([V])
    visited = []
    while queue:
        item = queue.popleft()
        if item not in visited:
            queue.extend(sorted(graph[item]))
            visited.append(item)
    print(*visited)

dfs(V)
bfs(V)