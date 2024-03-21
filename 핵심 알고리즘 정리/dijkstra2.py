'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
import sys
sys.stdin = open('dijkstra.txt')

def dijkstra(start):
    U = []
    distance = [1e10] * V
    distance[start] = 0

    while len(U) != V:
        
        minV = 1e12
        for i in range(V): # 제일 작은 것을 골라서 가져간다. # heapq
            if i in U : continue
            if distance[i] < minV:
                minV = distance[i]
                now = i
        
        U.append(now)
        
        for i in range(V):
            if i in U: continue
            if graph[now][i]: # 간선끼리 비교해서 최대한 작은 값을 취하게 해준다.
                distance[i] = min(distance[i], distance[now]+graph[now][i])
                
    return distance, U

V, E = map(int, input().split())
# 인접행렬 사용
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    

print(dijkstra(0))