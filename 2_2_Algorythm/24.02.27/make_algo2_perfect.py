def brute_search(x):
    global permutation
    if x == N:
        P = []
        for i in range(N):
            P.append(path[i])
        permutation.append(P)
        return

    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        path.append(i)
        brute_search(x+1)
        path.pop()
        visited[i] = 0

def solve():
    global max_sum_value

    for order in permutation: # 만들어진 permutation을 가지고 쓴다.
        sum_value = 0
        row = 0
        for col in order:
            if matrix[row][col] >= 0:
                sum_value += matrix[row][col]
            else:
                sum_value = -1 # 터트린 풍선이 음수일 경우 바로 그 순열은 제외한다.
                break
            row += 1
        if max_sum_value < sum_value: # 각 순열 시행마다 최대값 갱신을 확인해준다.
            max_sum_value = sum_value
    return max_sum_value

import sys
sys.stdin = open("algo2_sample_in.txt")

# 순열 만드는 것이 아직 익숙치 않아 문제 풀이에 실패한 것 같다.
# 이것을 subset을 사용하는가? 그것은 힘들다고 본다.
# DFS 알고리즘이라고 이야기할 수 있는가?
T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    permutation = []
    N = int(input()) # 3이상 8이하
    matrix = [list(map(int, input().split())) for _ in range(N)] # 점수는 -100 이하
    path = []
    visited = [0] * (N+1)
    brute_search(0) # 완전 탐색을 사용하는 경우, N의 개수가 동일하고, 단순하면 쉽다.
    max_sum_value = 0


    print(f'#{tc} {solve()}')
