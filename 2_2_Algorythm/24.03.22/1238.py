
# Flood Fill Algorythm이랑 유사하다!!!

# Dictionary 풀이
from collections import deque
def BFS(s):

    q = deque([s])
    visited[s] = 1
    
    while q:
        item = q.popleft() # 들어갈 지점을 뽑아낸다.
        
        # for k in graph[item]: # graph[item]이 존재한다면, 갈 수 있는 간선의 개수를 돌면서 확인한다.
        #     if not visited[k]: # 해당 노드를 방문하지 않아, 간선을 돌지 않았다면
        #         visited[k] = visited[item] + 1 # 지금의 노드로부터 level+1에 해당 노드를 방문 처리하고
        #         q.append(k) # k를 queue에 추가해둬서 다시 while을 돌게 만든다.
        if item in graph_dict:
            for k in graph_dict[item]:
                if not visited[k]:
                    visited[k] = visited[item]+1
                    q.append(k)
        
    max_depth = max(visited)
    for i in range(100, -1, -1):
        if visited[i] == max_depth:
            return i

for tc in range(1, 11):
# for tc in range(1):
    E, start = map(int, input().split())
    fromto = list(map(int, input().split()))
    
    graph = [[] for _ in range(101)] # 0 ~ 100까지
    graph_dict = dict()
    visited = [0] * 101
    for e in range(E//2):
        graph_dict.setdefault(fromto[2*e], []).extend([fromto[2*e+1]])
        
        # if fromto[2*e+1] not in graph[fromto[2*e]]: # 중복 제거
        #     graph[fromto[2*e]].append(fromto[2*e+1])
    print(f'#{tc} {BFS(start)}')
    
'''
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2
'''