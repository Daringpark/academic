
def build_tree(preorder):
    if not preorder:
        return None

    root = preorder[0]
    left_subtree = [val for val in preorder[1:] if val < root]
    right_subtree = [val for val in preorder[1:] if val > root]

    left_child = build_tree(left_subtree) if left_subtree else None
    right_child = build_tree(right_subtree) if right_subtree else None

    return (root, left_child, right_child)
#
# def make_graph(lst): # 전위순회된 리스트를 받아서 그래프화 시킨다.
#     root = lst[0]
#     lt = []

# 전위순회는 VLR 후위순회는 LRV

numbers = []
for _ in range(10000): # 전위순회해서 받음
    try:
        numbers.append(int(input()))
    except: # 입력이 없을때 반복문에서 빠져나가기 EOFerror를 이용해도 되지만, 그냥 except 사용
        break
print(build_tree(numbers))

# print(make_graph(numbers))


'''
50
30
24
5
28
45
98
52
60
'''