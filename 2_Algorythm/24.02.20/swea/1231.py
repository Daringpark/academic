def LVR_binary_search(root):
    global res
    m = len(graph[root])
    if m >= 2: # 글자와 다른 자식 노드로
        LVR_binary_search(int(graph[root][1]))
    res += graph[root][0]
    if m == 3:
        LVR_binary_search(int(graph[root][2]))
T = 10
for tc in range(1, T+1):

    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N):
        per_node = list(input().split())
        graph[int(per_node.pop(0))].extend(per_node)
    res = ''
    LVR_binary_search(1)
    print(f'#{tc} {res}')
