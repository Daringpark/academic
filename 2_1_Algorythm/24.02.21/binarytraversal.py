def insert(data):
    idx = 1
    while TREE[idx]:
        if TREE[idx] > data:
            idx *= 2 # binary 내부 rt
        else :
            idx = idx*2+1 # binary 내부 lt

    TREE[idx] = data
    print(TREE[idx])

def find(key):
    idx = 1
    while TREE[idx]:
        if TREE[idx] == key:
            return idx

        if TREE[idx] < key:
            idx = 2*idx + 1
        else : idx *= 2
    return -1


numbers = [9,4,12,3,6,15,13,17]
N = len(numbers)
TREE = [0] * (max(numbers)+1)
for i in numbers:
    insert(i)
print(TREE)
print(find(3))
print(find(7))
print(find(13))

def enqueue(data):
    global last
    last += 1
    TREE[last] = data
    c = last
    p = last//2
    while p:
        if TREE[p] > TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            c = p
            p = c//2
        else:
            break
    print(TREE)
def solve():
    idx = N
    res = 0
    while idx != 1:
        idx //= 2
        res += TREE[idx]
        print(idx, res)
    return res

numbers = [20,4,15,19,13,11,12]
numbers = [18,57,11,52,14,45,63,40]
N = len(numbers)
TREE = [0] * (N+1)
last = 0
for i in numbers:
    enqueue(i)
print(solve())