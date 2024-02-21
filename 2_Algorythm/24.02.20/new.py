
matrix = [[0,0,0], [0,1,2]]
N = len(matrix)

for i in range(N):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
    print()

def make_graph():
    global graph
    arr = list(map(int, input().split()))
    for i in range(N+1):
        if i != N:
            for j in range(20):
                graph[i].append(arr[20*i+j])
        else:
            for j in range(number%20):
                graph[i].append(arr[20*i+j])



number = 48
N = number // 20
graph = [[] for _ in  range(N+1)]
make_graph()

print(graph)