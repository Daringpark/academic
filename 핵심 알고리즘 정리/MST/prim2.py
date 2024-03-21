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

def prim(start):
    U = []
    distance = [1e10] * V
    distance[start] = 0

    while len(U) != V:
        
        minV = 1e8
        for i in range(V): # 제일 작은 것을 골라서 가져간다. # heapq
            if i in U : continue
            if distance[i] < minV:
                minV = distance[i]
                now = i
        
        U.append(now)
        print(now)
        
        for i in range(V):
            if i in U: continue
            if graph[now][i]: # 간선끼리 비교해서 최대한 작은 값을 취하게 해준다.
                distance[i] = min(distance[i], graph[now][i])
                
    return distance, U

V, E = map(int, input().split())
# 인접행렬 사용
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w
    

print(prim(0))