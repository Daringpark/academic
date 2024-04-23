
# BOJ 15900 나무 탈출 실버 1
import sys
input = sys.stdin.readline
# N <= 500000
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

# 1. graph making
for _ in range(N-1):
    s, e = map(int, input().split())

    if e not in graph[s]:
        graph[s].append(e)

    if s not in graph[e]:
        graph[e].append(s)

# 2. main function DFS (stack)
def dfs():
    # leaf-node counts
    cnt = 0

    stack = []
    stack.append(1)

    while stack:
        # 1 2
        item = stack.pop()

        # 3. 지금 꺼낸 item의 노드가 leaf노드인가를 판별할 수 있어야 함.
        if item != 1 and len(graph[item]) == 1:
            cnt += 1

        # 3-2. 순회하면서 stack에 추가
        for new_item in graph[item]:
            if not visited[new_item]:
                visited[new_item] = 1
                stack.append(new_item)
                
# 1 2 3, 1 2 4
    # print(cnt)
    if cnt%2:
        return 'Yes'
    return 'No'

# print(graph)
# 4. result, root-leaf%2 == True : Yes; No
print(dfs())
# 1 W, 2 L, 4 L
    
'''
8
8 1
1 4
7 4
6 4
6 5
1 3
2 3

  1
3 4 8(4)
2(1) 7(2) 6
  5(3)

'''

'''
8
1 2
6 2
3 2
3 7
4 3
8 4
4 5
'''