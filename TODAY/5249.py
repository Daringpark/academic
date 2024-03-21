import sys
sys.stdin = open("5249.txt")


from heapq import heappush, heappop

def prim(start):
    pq = []
    visited = [0] * (V+1)
    
    # 최종 가중치
    sum_weight = 0
    
    # heapqueue를 시작값으로 채우고 시작
    heappush(pq, (0, start))
    
    while pq:
        weight, now = heappop(pq)
        if visited[now]:
            continue
        
        visited[now] = 1
        sum_weight += weight
        
        n = len(graph[now])
        for i in range(n):
            node_n = graph[now][i][0]
            weight_n = graph[now][i][1]
            
            if weight_n and not visited[node_n]:
                heappush(pq, (weight_n, node_n))
    return sum_weight

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)] # 0 ~ V까지
    # 최소 신장 트리 # 무향 그래프
    # Linked_List
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])
        graph[e].append([s, w])
    print(f'#{tc} {prim(0)}')
    
'''
1
2 3
0 1 1
0 2 1
1 2 6
'''