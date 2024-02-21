# LVR 순회
def pre_order(root): # 값 채워 넣기
    global i
    if 2*root <= N:
        pre_order(2*root)
    TREE_AMOUNT[root] = i
    i += 1
    if 2*root +1 <= N:
        pre_order(2*root+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # number = 6
    TREE_AMOUNT = [0] * (N+1) # 0 1 2 3 4 5 6
    # root = 1
    # N//2 = 3
    i = 1
    pre_order(1)
    print(f'#{tc} {TREE_AMOUNT[1]} {TREE_AMOUNT[N//2]}')