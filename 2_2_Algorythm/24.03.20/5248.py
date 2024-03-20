
'''
1
7 4
2 3 4 5 4 6 7 4
'''
def dfs(): # 인접 영역 확인하기
    global visited, cnt
    
    for i in range(1, N):
        if not visited[i]:
            
            stack = [i]
            while stack:
                item = stack.pop()
                visited[item] = 1
                
                new_idx = item + 1
                if new_idx < N and not visited[new_idx]:
                    if arr[item] == arr[new_idx]: # 인접해 있다면
                        stack.append(new_idx)
                        visited[new_idx] = 1
            cnt += 1


T = int(input())

for tc in range(1, T+1):
    
    N, k = map(int, input().split()) # N은 2이상
    edge = list(map(int, input().split()))
    arr = [0] * (N+1)
    visited = [0] * (N+1)
    idx = 1
    
    # 인접한 영역 만들기
    for i in range(k):
        start, end = edge[2*i], edge[2*i+1]
        if arr[start] or arr[end]:
            number = max(arr[start], arr[end])
            arr[end] = arr[start] = number
        elif not arr[start]:
            arr[start] = arr[end] = idx
            idx += 1
    # 이렇게 인접 영역을 만들면, 탐색할때 매우 어려움 (점프 뛰기 어려움)      
    
    cnt = 0
    dfs()
    print(f'#{tc} {cnt}')