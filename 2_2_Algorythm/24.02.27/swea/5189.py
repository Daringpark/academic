import sys
sys.stdin = open("5189.txt")
########## 공부 필요


def make_permutation(k, s): # k 0,1,2
    global total_min_value
    if s > total_min_value:
        return
    if k == N-1:
        # path1 = [0] + path + [0]
        s = s + Matrix[path[k-1]][path[k]] # k == N-1 마지막에 추가를 해줘야 함.
        if s < total_min_value:
            total_min_value = s
        return
    for i in range(N): # 0, 1, 2
        if not visited[i]:
            path[k] = i
            visited[i] = 1
            start = path[k-1]
            end = path[k] # i
            make_permutation(k+1, s + Matrix[start][end])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Matrix = [list(map(int, input().split())) for _ in range(N)]
    path = [0] * N
    visited = [0] * N
    total_min_value = 1e10
    visited[0] = 1
    make_permutation(0, 0)
    print(f'#{tc} {total_min_value}')




