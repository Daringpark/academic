import sys
sys.stdin = open('route.txt')
# 기존과 같은 방식으로 DFS 했을 경우

def make():
    global N
    full = list(map(int, input().split()))
    for i in range(N):
        if full[2*i] not in graph:
            graph[full[2*i]] = [full[2*i+1]]
        else:
            graph[full[2 * i]].append(full[2*i+1])
    return graph

def solve():
    visited = []
    unvisited = [0]
    goal = 99
    while unvisited:
        node = unvisited.pop()
        if node in graph:
            unvisited.extend(graph[node])
        if node not in visited:
            visited.append(node)
        if 99 in visited:
            break
    if goal in visited:
        return 1
    else : return 0

for _ in range(10):
    tc, N = map(int, input().split())
    graph = {}
    make()
    print(f'#{tc} {solve()}')