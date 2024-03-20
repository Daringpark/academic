
from collections import deque

def bfs(num):
    queue = deque()
    # 초기 세팅
    visited[num] = 1
    queue.append(num)

    # bfs 돌기
    while queue:
        item = queue.popleft()
        # if item < 1 and item > 1e6: # 범위 밖이면 나가세요
        #     continue
        if item == goal:
            return visited[item]-1
        
        for k in [1, -1, item, -10]:
            new_item = item + k
            if 1 <= new_item <= 1e6 and not visited[new_item]:
                visited[new_item] = visited[item] + 1
                queue.append(new_item)


T = int(input())
for tc in range(1, T+1):
    number, goal = map(int, input().split())
    # +1, -1, *2, -10 4가지 연산을 진행할 수 있다.
    # number가 백만 이상으로 넘어가면 안된다.
    visited = [0] * int(1e6+1)
    print(f'#{tc} {bfs(number)}')
    # print(visited)
    
'''
3
2 7
3 15
36 1007
'''