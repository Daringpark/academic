
'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''

# N, M, V ; 정점(노드)의 개수, 간선(엣지)의 개수, 시작할 정점의 번호

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline


# 여러 자식 노드가 나왔을 경우, 그 값에서 제일 작은 값을 우선순위로 봐야한다는 점이 가장 크다.
def dfs():
    global lst1
    line = []
    visited = []
    line.append(V)
    while line:
        item = line.pop()
        if item not in visited:
            visited.append(item)
            line.extend(lst1[item])
    return ' '.join(map(str, visited))

def bfs():



N, M, V = map(int, input().split())

graph = [[] for _ in range(1001)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
lst1 = deepcopy(graph)
lst2 = deepcopy(graph)
print(dfs())
