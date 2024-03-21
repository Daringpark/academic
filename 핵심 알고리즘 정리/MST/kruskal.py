
# 간선을 하나씩 선택해서 MST를 찾는 알고리즘
# 1. 최초, 모든 간선을 가중치에 따라서 오름차순으로 정렬
# 2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킨다.
# 만약 사이클이 존재한다면, 다음으로 가중치가 낮은 간선 선택
# N-1개의 간선이 선택될 때까지 2.를 반복한다.


import sys
sys.stdin = open("input.txt")

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x, y = find_set(x), find_set(y)
    if x == y :
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

V, E = map(int, input().split())
# 인접행렬 사용
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s,e,w])
edges.sort(key = lambda x: x[2])
parents = [i for i in range(V)]

sum_weight = 0
cnt = 0
print(f'{parents} : {sum_weight} : {cnt}')
for s, e, w in edges:
    if find_set(s) == find_set(e):
        print("Cycle!")
        continue
    
    cnt += 1
    union(s, e)
    sum_weight += w
    print(f'{parents} : {sum_weight} : {cnt}')
    
    # 의미 없는 Cycle을 돌지 않게 만들어준다.
    if cnt == V-1:
        break