import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


from collections import deque
def bfs(num):
    # 마지막에 연락 받으면서, 그 중 가장 숫자가 큰 사람을 선택하시오
    
    q = deque([[num]])
    cnt = 1
    while q: # [[7,15]]
        temp = []
        item = q.popleft() # [7, 15]
        
        for k in item: # 7 15
            if not visited[k]: # visited[2] == 0
                temp.extend(graph[k]) # [[100], [4]]
                visited[k] = cnt # 2 item == [2]
        q.append(temp)
        cnt += 1
        if not temp:
            break
    
    for i in range(100, -1, -1):
        if visited[i] == max(visited):
            return i

for tc in range(1, 11):
# for tc in range(1):
    
    N, call = map(int, input().split())
    fromto = list(map(int, input().split()))
    graph = [[] for _ in range(101)] # 번호 1이상 100 이하
    visited = [0] * 101
    for i in range(N//2):
        start, end = fromto[2*i], fromto[2*i+1]
        graph[start].append(end)

    print(f'#{tc} {bfs(call)}')
    
'''
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2


'''