import sys
sys.stdin = open("input_5117.txt")

def min_heap(data):
    global pos
    pos += 1
    TREE[pos] = data
    c = pos # 첫 자식은 1,// 2, 3,// 4, 5, 6, 7,// 8, 9, 10, 11
    p = pos//2 # 부모는 0,// 1, 1,// 2, 2, 3, 3,// 4, 4, 5, 5
    while p: # 아래서부터 타고 올라가는 특징 힙 정렬
        if TREE[c] < TREE[p]: # 트리의 부모가 트리의 자식보다 높으면 값을 내려준다.
            TREE[c], TREE[p] = TREE[p], TREE[c]
            c = p
            p = c//2
        else:
            break

def solve():
    idx = node_N
    res = 0
    while idx != 1:
        idx = idx//2 # 제일 마지막 잎 노드를 기준으로 조상 노드들의 합을 받는다.
        res += TREE[idx]
    return res

T = int(input())
for tc in range(1, T+1):
    node_N = int(input())
    order = list(map(int, input().split()))
    TREE = [0] * (node_N+1) # 완전 이진 트리의 경우 노드 개수 + 1 (0번째 제외)
    # heapify # 더 간단한 구현이 가능할까
    pos = 0
    for i in order:
        min_heap(i)
    print(f'#{tc} {solve()}')

