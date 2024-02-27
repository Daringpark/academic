

def reach_ten(x):
    # if x == 1001: # recursive depth error
    if x == 11:
        return
    # 트리 탐색 LVR 재귀 탐색이랑 비슷하게 출력+재귀+출력 구조로
    print(x, end = ' ')
    reach_ten(x+1)
    print(x, end = ' ')
reach_ten(0)
print()

### 중복이 포함된 중복순열 리스트 (재귀 구현)
path = []
def path_finding(x):
    if x == 3: # level이 맞을 때
        print(' '.join(map(str, path)))
        return
    for i in range(1, 7):
        path.append(i)
        path_finding(x + 1)
        path.pop()
path_finding(0)

path = []
def path_finding(x):
    if x == 5: # level이 맞을 때
        print(' '.join(map(str, path)))
        return
    for i in range(1, 5):
        path.append(i)
        path_finding(x + 1)
        path.pop()
path_finding(0)
print()

def die(x, die_number, type_number):
    if type_number == 1: # 중복 순열로 뽑게
        if x == die_number:
            print(' '.join(map(str, path)))
            return
        for i in range(1, 7):
            path.append(i)
            die(x+1, die_number, type_number)
            path.pop()

    elif type_number == 2:
        if x == die_number:
            print(' '.join(map(str, path)))
            return
        for i in range(1, 7):
            if visited[i]: continue
            visited[i] = 1
            path.append(i)
            die(x+1 , die_number, type_number)
            path.pop()
            visited[i] = 0
N, Type = map(int, input().split())
path = []
visited = [0] * 7
die(0, N, Type)














