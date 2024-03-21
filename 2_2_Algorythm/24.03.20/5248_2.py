# 출석번호 인덱스까지 parent리스트 만들어주기 (0번은 사용안함)
def make_set(n):
    return list(range(n + 1))

# find: x를 포함하는 집합을 찾는 연산
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

# union: x와 y를 포함하는 두 집합을 통합하는 연산
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    parent[root_x] = root_y

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    # 부모를 자기 자신으로 정의
    parent = make_set(N)

    # u <-> v 연결된 두 정점을 하나의 그룹으로 합해준다.
    for i in range(M):
        v = L[i * 2]
        u = L[i * 2 + 1]
        union(v, u)

    result = set()

    # 정점의 갯수가 몇개인지 set 자료형을 사용하여 카운트
    for i in range(1, N + 1):
        result.add(find_set(i))

    print(f"#{tc} {len(result)}")
