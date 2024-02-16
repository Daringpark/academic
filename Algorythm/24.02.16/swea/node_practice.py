import sys
sys.stdin = open('node.txt')

def graph():
    global node_list
    for _ in range(E):
        start, end = map(int, input().split())
        node_list[start-1].append(end)
        node_list[end-1].append(start)
def bfs(): # 0 ~ V-1 번째 노드까지
    start, end = map(int, input().split())
    Q = []
    depth = [0]*V
    Q.append(start-1)
    while Q:
        item = Q.pop(0)
        for w in node_list[item]:
            if not depth[w-1]:
                Q.append(w-1)
                depth[w-1] = depth[item]+1
            if depth[end-1]: # 조기 종료 확인
                return depth[end-1]
    return 0 # 도달할 수 없다면
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V는 node개수, 5줄에 걸쳐 출발과 도착선을 만들어준다.
    node_list = [[] for _ in range(V)]
    graph()
    print(f'#{tc} {bfs()}')