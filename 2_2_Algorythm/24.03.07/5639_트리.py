
import sys
sys.setrecursionlimit(2*10**5)

def build_tree(preorder): # 전위순회로 받은 리스트를 그래프로 그린다.
    if not preorder: # 자식루트에 도달했을 경우
        return None
    root = preorder[0]
    left_subtree = [val for val in preorder[1:] if val < root]
    right_subtree = [val for val in preorder[1:] if val > root]
    left_child = build_tree(left_subtree) if left_subtree else None # 왼쪽에 넣을 값이 있다면
    right_child = build_tree(right_subtree) if right_subtree else None # 오른쪽에 넣을 값이 있다면
    return [root, left_child, right_child]

# 순회 LRV
def postorder(graph): #node, left, right
    if not graph[0]:
        return
    if graph[1]:
        postorder(graph[1]) # left node
    if graph[2]:
        postorder(graph[2]) # right node
    print(graph[0])

# 전위순회는 VLR 후위순회는 LRV
numbers = []
for _ in range(10000): # 전위순회해서 받음
    try:
        numbers.append(int(input()))
    except: # 입력이 없을때 반복문에서 빠져나가기 EOFerror를 이용해도 되지만, 그냥 except 사용
        break
Tree = build_tree(numbers)
postorder(Tree)


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