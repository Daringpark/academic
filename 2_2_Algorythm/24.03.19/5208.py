

'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

1
3 2 0 1
'''
def stepbystep(point, charge):
    global min_cnt
    # global cnt # 디버깅용
    
    # 최소 값을 넘어갔을 경우, 그건 return
    if charge > min_cnt: # 최소 한번을 돌고 나서 백트래킹이 가능하다
        return
    # 이 경우 싹 다 돌아버리는 것 같은데
    
    # 인덱스가 값에 도착 혹은 그것을 넘어 갈 경우
    if point >= N:
    # 1회의 충전으로 도착 혹은 넘을 경우
        min_cnt = min(min_cnt, charge)
        return
    
    if stop[point] != 0: # 배터리 용량이 0이면 그 자리에서 멈추게 된다.
        for i in range(1, stop[point]+1): # 용량만큼
            # 하나하나씩 더해주는 경우, 최악은 2의 배터리 용량 중 첫번째를 골랐을 때 1*N으로 가는 경우를 세는 등
            if charge+1 < min_cnt:
                # cnt += 1
                stepbystep(point+i , charge+1) # 하나하나 더해준다....
    
T = int(input())
for tc in range(1, T+1):
    
    stop = list(map(int, input().split())) + [0]
    N = stop[0]
    # step = stop[1] # 초기 스텝
    min_cnt = 101
    # 1번에서 출발 종점은 N번
    # cnt = 0 # 디버깅용
    stepbystep(1, -1) # 처음 충전은 생각하지 않는다.
    # 초기 배터리가 0인 경우는 고려하지 않는다. (아예 운행을 못하는 경우)
    
    print(f'#{tc} {min_cnt}')