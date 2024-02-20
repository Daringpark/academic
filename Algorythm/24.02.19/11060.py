'''
10
1 2 0 1 3 2 1 5 4 2
'''




from collections import deque




def make_graph():
    global graph
    for i in range(N): # 0 ~ 9 까지 확인하기
        amount = maze[i]
        if amount > 0:
            for j in range(1, amount+1):
                graph[i+1].append((i+1+j))

def BFS():
    # 그려진 그래프에서 Queue를 활용한 BFS를 한다.

    line = deque()








N = int(int(input()))
maze = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

print(maze)
print(graph)
make_graph()
print(graph)


