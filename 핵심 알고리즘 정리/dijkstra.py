
# 최단 경로 정의
# 3가지 알고리즘이 존재한다.
# dijkstra, Bellman-Ford, Floyd-warshall

# dijkstra 알고리즘은 그럼 뭔가?
# 시작 정점에서 끝 정점까지의 최단 경로를 뽑을 수 있다.
# 하지만, 음의 가중치는 고려하지 않는다는게 특징이다.
# 간선의 가중치와 지금까지의 누적 가중치 등을 비교하였을 때, 더 작은 것을 뽑아야하니까

import heapq
import sys
sys.stdin = open('dijkstra.txt')

def dijkstra(start):
    hq = []
    
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    
    while hq:
        dis, now = heapq.heappop(hq)
        if distance[now] < dis: # 필요 없는 계산처리를 하지 않고 다시 Queue pop
            continue
        
        # 현재 노드에서 다음 노드를 확인
        for k in graph[now]:
            next_dis = k[0]
            next_node = k[1]
            
            new_dist = dis + next_dis
            if new_dist >= distance[next_node]:
                continue
            distance[next_node] = new_dist
            heapq.heappush(hq, (new_dist, next_node))



limit = int(1e10) # 누적 거리보다 더 큰 값
V, E = map(int, input().split())
graph = [[] for _ in range(V)]
distance = [limit] * V
start = 0

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e]) # 단향 그래프

dijkstra(0)
print(distance)