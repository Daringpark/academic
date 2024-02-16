

def graph(ls):
    route = list(map(int, ls.split()))
    M = len(route)
    our_graph = [0] * (M//2) # 0 ~ 4
    for i in range(M//2): # 14//2 = 7 0~6까지
        our_graph[i] = [route[2*i], route[2*i+1]]
    return our_graph



# def bfs(s):
#     Q = []
#     visited = [0] * (N+1)
#
#     Q.append(s)
#     visited[s] = True
#     while Q:
#         v = Q.pop(0) # 시작 지점
#         print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = True


N, E = 5, 14
lst = '1 3 2 4 1 2 3 5 1 2 3 4 4 5'



print(graph(lst))