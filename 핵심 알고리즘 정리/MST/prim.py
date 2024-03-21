'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
import sys
sys.stdin = open("input.txt")

import heapq

def prim(start):

    hq = []
    visited = [0] * V

    # 최소 비용을 계산해준다.
    sum_weight = 0
    
    # 튜플로 관리하면 여러 특성을 사용할 때는 클래스를 사용하는게 좋다.
    heapq.heappush(hq, (0, start))

    while hq:
        weight, now = heapq.heappop(hq)
        
        if visited[now]: # 내가 방문했던 곳이면 그 곳으로 가는 최소 비용 간선은 생각하면 안된다.
            continue
        
        visited[now] = 1
        print(f'{visited} : {now} : {weight}')
        sum_weight += weight
        
        
        for i in range(V):
            # 값이 있으면서, 내가 방문하지 않았다면    
            if graph[now][i] and not visited[i]:
                heapq.heappush(hq, (graph[now][i], i))
                
    
    
    return sum_weight
                
    


V, E = map(int, input().split())
# 인접행렬 사용
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w

for i in range(V):
    print(*graph[i])
    
print(prim(3))