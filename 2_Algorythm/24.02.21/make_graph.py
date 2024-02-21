import copy

def insert(data): # 필요없는 더미 0 데이터가 무수히 생김
    idx = 1
    while TREE[idx]:
        if TREE[idx] > data:
            idx *= 2 # binary 내부 rt
        else :
            idx = idx*2+1 # binary 내부 lt

    TREE[idx] = data
    print(TREE[idx])

def enqueue_0(data):  # 입력을 받아 그래프로 저장
    global last
    last += 1
    TREE_0[last] = data

def enqueue_1(data): # 정렬된 최소힙 생성
    global last
    last += 1
    TREE[last] = data
    c = last
    p = last//2
    
    while p: # 최소힙 생성 위치
        if TREE[p] > TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            c = p
            p = c//2
        else:
            break
    print(TREE)

numbers = [18,57,11,52,14,45,63,40]
TREE = [0] * (len(numbers)+1)
TREE_0 = copy.deepcopy(TREE)
TREE_1 = copy.deepcopy(TREE)
last = 0
for i in numbers:
    enqueue_0(i)
print(TREE_0) # last를 이용한 데이터 불러오기 # 힙 정렬이 가능함
print([0] + numbers) # list-map으로 불러오는 경우
