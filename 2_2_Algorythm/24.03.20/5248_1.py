
'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''
def dfs(): # 인접 영역 확인하기
    global visited, cnt
    
    for i in range(1, N+1):
        
        if not visited[i]:
            cnt += 1
            visited[i] = 1
            
            if graph[i]:    
                stack = graph[i]
                while stack:
                    item = stack.pop()
                    if not visited[item]:
                        stack.extend(graph[item])
                        visited[item] = 1

T = int(input())
for tc in range(1, T+1):
    
    N, k = map(int, input().split()) # N은 2이상
    edge = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    
    for i in range(k):
        start, end = edge[2*i], edge[2*i+1]
        graph[start].append(end)
        graph[end].append(start)

    cnt = 0
    dfs()
    
    print(f'#{tc} {cnt}')