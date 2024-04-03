import sys
# sys.stdin = open("algo2_sample_in.txt", "r")
def dfs1(level, sum_cost, cnt):
    global max_bridge
    global min_cost
    if sum_cost > V: # 예산이 초과하면 탈락
        return

    if level == N: # 섬을 다 연결하면 return
        if max_bridge < cnt:
            max_bridge = cnt
            min_cost = min(min_cost, sum_cost)
        elif max_bridge == cnt:
            min_cost = min(min_cost, sum_cost)
        return

    dfs1(level+1, sum_cost+cost_list[level], cnt+1)
    dfs1(level+1, sum_cost, cnt)


'''
1
10 75
1 1 1 1 1 65 21 17 19 40

8 62
'''
# 월말 2번 combination

def dfs2(level, start):
    global max_bridge
    global min_cost
    global sum_cost
    global cnt
    if sum_cost > V:  # 예산이 초과하면 탈락
        return

    if level == N:  # 섬을 다 연결하면 return
        if max_bridge < cnt:
            max_bridge = cnt
            min_cost = min(min_cost, sum_cost)
        elif max_bridge == cnt:
            min_cost = min(min_cost, sum_cost)
        return

    if not visited[level]:
        sum_cost += cost_list[level]
        visited[level] = 1
        cnt += 1
        dfs2(level+1)
        visited[level] = 0
        sum_cost -= cost_list[level]
        cnt -= 1
        dfs2(level+1)

T = int(input())
for tc in range(1, T+1):
    N, V = map(int, input().split()) # N = 섬의 수, V = 예산
    cost_list = list(map(int, input().split()))
    max_bridge = 0
    min_cost = float('inf')
    sum_cost = 0
    cnt = 0
    visited = [0] * N
    # dfs1(0, 0, 0)
    dfs2(0, 0)
    print(f'#{tc} {max_bridge} {min_cost}')
