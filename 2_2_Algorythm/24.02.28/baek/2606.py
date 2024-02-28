


'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
N = int(input()) # 노드의 갯수라고 이야기를 할 수 있겠다. range(1, N+1)
K = int(input()) # 그래프를 그리기 위해서 간선의 개수를 세준다.
visited = [0] * (N+1) # visited[1] 또한 1이기 때문에, 감염된 컴퓨터의 수를 세려면 x=visited.count(1) -1
graph = [[] for _ in range(N+1)]# 1 ~ N까지 + 0
for _ in range(K):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) # 양 방향을 고려하게 된다면, 이를 순회할 수 있다. 하지만 이게 DFS는 아니다
stack = [1] # DFS로 풀어보고자 한다.
while stack:
    item = stack.pop()
    if not visited[item]: # 이 부분을 수정해야할 것 같다.
        visited[item] = 1
        if graph[item]:
            stack.extend(graph[item]) # append를 하게 되면 [[], graph[item]]
print(visited.count(1)-1)

#### DFS 방식으로 풀 수 있는가?
#### BFS 방식으로 풀 수 있는가?








