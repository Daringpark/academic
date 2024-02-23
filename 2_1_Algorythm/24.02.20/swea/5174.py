def count_node(new_node):
    global COUNTS
    if graph[new_node]:
        if len(graph[new_node]) >= 1:
            COUNTS += 1
            count_node(graph[new_node][0])
        if len(graph[new_node]) == 2:
            COUNTS += 1
            count_node(graph[new_node][1])
T = int(input())
for tc in range(1, T+1):
    E, root = map(int,input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(max(arr)+1)]
    for i in range(E):
        t, c = arr[2*i], arr[2*i+1]
        graph[t].append(c)
    COUNTS = 1
    count_node(root)

    print(f'#{tc} {COUNTS}')