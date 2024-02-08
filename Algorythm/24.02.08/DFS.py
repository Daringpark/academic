import sys
sys.stdin = open('dfs.txt.')

def make(): # 딕셔너리로 만들어 줌
    global graph
    for _ in range(E):
        s, e = map(int, input().split())
        if s not in graph: # setdefault
            graph[s] = []
        if e not in graph:
            graph[e] = []
        graph[s].append(e) # 아래로 내려가면서 순회
        # graph[e].append(s) # 이 열을 추가하지 않아도 자동으로 DFS, BFS를 할 수 있음
    return graph
def solve():
    start, goal = map(int, input().split()) # 시작 지점과 목표 지점과의 노드 연결성
    unvisited, visited = [], [] # 두개의 리스트를 활용하여 체크
    unvisited.append(start) # 시작 지점에서의
    while unvisited: # 모든 경로를 순회하도록
        node = unvisited.pop()
        if node not in visited:
            visited.append(node)
            unvisited.extend(graph[node])
    if start in visited and goal in visited:
        return 1
    else: return 0

T = int(input())
for tc in range(1, T+1):
    graph = {}
    V, E = map(int, input().split())
    make() # 공간 만들기
    print(f'#{tc} {solve()}')