

def make_graph(ls):
    global graph
    route = list(map(int, ls.split()))
    M = len(route)
    our_graph = [0] * (M//2) # 0 ~ 4
    for i in range(M//2): # 14//2 = 7 0~6까지
        our_graph[i] = [route[2*i], route[2*i+1]]
    for i in range(M//2):
        graph[our_graph[i][0]].append(our_graph[i][1])

def bfs(s):
    Q = []
    visited = [0] * (N+1)

    Q.append(s)
    visited[s] = True
    while Q:
        v = Q.pop(0) # 시작 지점
        print(v)

        for w in graph[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = True

N, E = 5, 12
lst = '1 3 2 4 1 2 3 5 3 4 4 5'


graph = [[] for _ in range(N+1)]
make_graph(lst)
print(graph)

print(bfs(1))