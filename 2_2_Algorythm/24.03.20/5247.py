
from collections import deque

def bfs(num):
    queue = deque()
    step = []
    # 초기 세팅
    visited[num] = 1
    for i in oper:
        if i > 1:
            visited[num*2] = 2
            queue.append(num*2)
        else:
            if 0 <= num+i < goal:
                visited[num+i] = 2
                queue.append(num+i)
    
    # bfs 돌기
    while queue:
        item = queue.popleft()
        if item < 1 and item > 1e6: # 범위 밖이면 나가세요
            continue
        
        for i in oper:
            if i > 1:
                if 1 <= item*2 < goal+1:
                    if visited[item*2] == -1: # 초기에 값이 없었다면,
                        visited[item*2] = visited[item]+1
                        queue.append(item*2)
                    else:
                        if visited[item*2] > visited[item]:
                            visited[item*2] = visited[item]
            else:
                if 1 <= item+i < goal+1:
                    
                    if visited[item+i] == -1: # 초기에 값이 없었다면,
                        visited[item+i] = visited[item]+1
                        queue.append(item+i)
                    else: # 더 나은 값이 온다면?
                        if visited[item+i] > visited[item]:
                            visited[item+i] = visited[item]
    
    return visited[goal]


oper = [2, 1, -1, -10]
T = int(input())
for tc in range(1, T+1):
    
    number, goal = map(int, input().split())
    # +1, -1, *2, -10 4가지 연산을 진행할 수 있다.
    # number가 백만 이상으로 넘어가면 안된다.
    visited = [-1] * int(1e6+1)
    print(f'#{tc} {bfs(number)-1}')
    # print(visited)
    
'''
3
2 7
3 15
36 1007
'''