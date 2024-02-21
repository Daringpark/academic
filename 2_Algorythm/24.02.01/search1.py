
## 순차 검색
def sequential_search(lst, n, key):
    i = 0
    while i < n and lst[i] != key:
        i += 1
    if i < n : return i # 존재하고, n을 넘지 않는 i일 때(길이 안에서 원소 탐색시)
    return -1 # 존재하지 않을 때

A = [10, 8, 23, 21, 4, 9, 6, 17, 32]
N = len(A)

print(sequential_search(A, N, 9)) # [10, 8, 23, 21, 4, 9, 6, 17, 32]
print(sequential_search(A, N, 11)) # 11은 A list 내에 없음
print('='*15)
## 순차 검색2 (정렬이 이뤄진 경우)
A.sort()
def sequential_search2(lst, n, key):
    i = 0
    while i < n and lst[i] < key: # 정렬되어 있기 때문에
        i += 1
    if i < n and lst[i] == key :
        return i
    else: # 검색 조기 종료
        return -1

print(sequential_search2(A, N, 17)) # [4, 6, 8, 9, 10, 17, 21, 23, 32]
print(sequential_search2(A, N, 13))
print('='*15)
## 이진 탐색 (BS)

def binary_search1(lst, n, key):
    lt = 0
    rt = n-1
    while lt <= rt:
        node = (lt+rt)//2
        if lst[node] == key:
            return True
        elif lst[node] > key:
            rt = rt -1
        else :
            lt = lt +1
    return False

print(binary_search1(A, N, 21)) # [4, 6, 8, 9, 10, 17, 21, 23, 32]
print(binary_search1(A, N, 13)) # 10과 17의 차이는 8 + 1회를 통해서 lt>rt 일때 False
print('='*15)

def binary_search2(lst, lt, rt, key): #재귀로 풀이
    if lt > rt: # 앞 탐색이 뒷 탐색을 추월하는 경우 결과 없음. 탐색 종료
        return False
    else:
        middle = (lt+rt)//2
        if key == lst[middle]: # 검색 성공
            return True
        elif key > lst[middle]:
            return binary_search2(lst, middle+1, rt, key)
        elif key < lst[middle]:
            return binary_search2(lst, lt, middle-1, key)

print(binary_search2(A, 0, N-1, 21)) # [4, 6, 8, 9, 10, 17, 21, 23, 32]
print(binary_search2(A, 0, N-1, 13))
print('='*15)
