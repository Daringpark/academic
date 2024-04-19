
# 백준 9934 완전 이진 트리
'''
2
2 1 3
LVR로 받았고, 이것을 트리 그래프를 출력으로 뽑아 내야한다. K = depth; level
'''
def down_to_depth():


    return 1

K = int(input())
LVR = list(map(int, input().split()))
root_idx = 2**K//2-1
root = LVR[2**K//2-1]

print(root)
# 출력단이
# root 3
# LR 1 5
# LR LR 0 2 4 6
# LR LR LR LR
# 이런식으로 출력되어야 한다