

import sys
sys.stdin = open("input_5178.txt")

def make_sum():
    global TREE
    pos = N
    if pos%2: # 나머지가 1이다. == 두 개가 존재
        TREE[pos//2] = TREE[pos-1] + TREE[pos]
    else: TREE[pos//2] = TREE[pos]
    while not TREE[1]: # 1번에 값이 있을 때까지,
        pos -= 1
        if TREE[pos//2]:
            pass
        else:
            TREE[pos // 2] = TREE[pos - 1] + TREE[pos]
    # LRV # 재귀 후위 순회로도 구현할 수 있다.

T = int(input())
# T = 1
for tc in range(1, T+1):
    # N, M, L = 5, 3, 2
    N, M, L = map(int, input().split())
    TREE = [0] * (N+1) # 완전 이진 트리
    # M줄에 거쳐서 리프 노드의 번호와 노드의 해당하는 값을 주어준다.
    for _ in range(M):
        node_number, amount = map(int, input().split())
        TREE[node_number] = amount
    make_sum()
    print(f'#{tc} {TREE[L]}')


