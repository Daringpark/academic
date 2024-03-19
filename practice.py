
# 예제 코드 // Permutation
# N = 4
# K = 2
# arr = [1,2,3,4]
# path = [0] * K
# def choice(n):
#     if n == K: # 재귀 leveling permutation
#         print(*path)
#         return
    
#     for i in range(len(arr)): # arr의 길이만큼을 그래야 가능
#         if arr[i] in path: # 값 자체를 받아야함
#             continue
#         path[n] = arr[i]
#         choice(n+1) # 재귀를 들어갔다가 빠져나오고 나서
#         path[n] = 0 # 원복해주는 과정이 무조건 필요함
# choice(0)

# 중복이 존재하는 Permutation
# def choice(n):
#     global res
#     if n == 3:
#         print(*res)
#         return

#     # 0 1 2
#     for i in range(1,4):
#         res.append(i)
#         choice(n+1)
#         res.pop()
# res = []
# choice(0)

# 중복이 존재하지 않는 Permutation
# 3 2 1 3!
# def choice(n):
#     global res
#     if n == 3:
#         print(*res)
#         return

#     # 0 1 2
#     for i in range(1,4):
#         if i not in res:
#             res.append(i)
#             choice(n+1)
#             res.pop()
# res = []
# choice(0)

# P인 이유
# def choice(n):
#     global res
#     if n == 2: # 4P2 = 4*3 = 12
#         print(*res)
#         return

#     # 0 1
#     for i in range(1,5): # 1 2 3 4
#         if i in res: # continue를 활용해서 반복문을 돌릴 수 있도록
#             continue
#         res.append(i) # 0, 1 == level
#         choice(n+1)
#         res.pop()
# res = []
# choice(0)


# Combination code
def combination(n, s): # 3가지 뽑기
    res
    if n == K: # 5C3 = 5 4 3 / 3 2 1 = 10
        print(*res)
        return
    
    for i in range(s, N):
        res[n] = i # level의 값
        combination(n+1, i+1)
    
arr = [1,2,3,4,5,6]
N = len(arr)
K = 3 # level
# visited = [-1] * N
res = [-1] * K

combination(0, 0) # 초기 단이 level 0이니까


# 도전 과제 : 1~10까지의 파워셋 중 중복 없는 합이 10인 자연수 부분 집합을 구하자.
# numbers = [i for i in range(1,11)]
# path = []
# pathlist = []
# def back(sumV):
#     global path, pathlist
    
#     if sumV > 10: # 바로 백트래킹
#       return  

#     if sumV == 10:
#         path = set(path) # 이런 처리를 안한다면?
#         if path not in pathlist:
#             pathlist.append(path)
#             print(*path)
#         path = list(path) # 이런 처리를 안하고 그냥 뽑는다면?
#         return

#     for num in numbers:
#         if num in path:
#             continue
#         path.append(num)
#         back(sumV + num)
#         path.pop()
# back(0)

# # Combination으로 만들고 싶어 나는...
# numbers = [i for i in range(1,11)]
# N = len(numbers)

# def back(start, sumV):
    
    
    
#   for i in range(start, N): # range를 사용하므로 +1
#     # n-k+level 최대 깊이 N - 내가 뽑을 갯수 K(limit) + 현재 깊이 level
#     arr[level] = A[i]
#     combi(level+1, i+1) 
    
# #### Tree
# # 간선의 s, e 포인트가 있을 때
# arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
# N = len(arr)//2 # 간선의 개수라고 이야기할 수 있다.

# # Class 사용하는 Tree만들기
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
    
#     def insert(self, child):
#         if not self.left:
#             self.left = child
#             return
        
#         if not self.right:
#             self.right = child
#             return
#         return
    
#     def LRV(self):
#         if self != None:
#             if self.left:
#                 self.left.LRV()
                
#             if self.right:
#                 self.right.LRV()
                
#             print(self.value, end = ' ')

# # 노드들을 생성하기
# nodes = [TreeNode(i) for i in range(max(arr)+1)]

# # 간선 연결하기
# for i in range(0, N):
#     parent_node = arr[2*i]
#     child_node = arr[2*i+1]
#     nodes[parent_node].insert(nodes[child_node])
# nodes[1].LRV()
# print()


# # linked list를 이용한 Tree만들기
# # 노드 만들기
# graph = [[] for _ in range(max(arr) + 1)]

# # 간선 연결하기
# for i in range(0, N):
#     graph[arr[2*i]].append(arr[2*i+1])

# # linked list를 만들어주기
# for i in range(len(graph)):
#     if len(graph[i]) != 2:
#         graph[i] = graph[i] + [None] * (2-len(graph[i]))
# # print(graph)

# def LRV(node):
#     if node == None: # linked list를 사용할 때 처리해야할 것
#         return
#     LRV(graph[node][0])
#     LRV(graph[node][1])
#     print(node, end = ' ')
# LRV(1)