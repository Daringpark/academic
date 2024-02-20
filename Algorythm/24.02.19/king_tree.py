'''
14
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13 6 14
'''
def pre_order(root):
    # if len(Tree[root]) >= 1:
    #     pre_order(Tree[root][0])
    # if len(Tree[root]) == 2: # 이진 트리의 경우 2
    #     pre_order(Tree[root][1])
    if Tree[root]:
        for i in range(len(Tree[root])): # 이진 트리가 아닌 경우, 자식 노드를 다 순회 하면서 확인
            pre_order(Tree[root][i])
    print(root)

N = int(input())
arr = list(map(int, input().split()))
Tree = [[] for _ in range(N+1)] # 간선의 개수만큼 2차원 배열로 만든다.


for i in range(len(arr)//2):
    p, c = arr[2*i], arr[2*i+1]
    Tree[p].append(c)
print(Tree)
pre_order(1)