# Binary_Search and Heap_Sort
# 있는 값만 뽑아 낼 때, 사용할 수 있는 이진 탐색
def binary_search(target):
    left = 0 # 값을 찾기 위해서
    right = len(arr)-1 # 인덱스 순서를 불러오기 위함
    cnt = 0

    while left <= right: # 왼쪽 오른쪽을 천천히 쪼일때, 왼쪽이 커지면 break
        mid = (left+right)//2
        cnt += 1
        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return -1, cnt

arr = [12,15,16,786,697,32014,534,123]
arr.sort()
print(arr)
X = 534
print(binary_search(X))

# 재귀 방식의 이진 탐색
cnt = 0
def Binary_search_recur(left, right, target):
    global cnt
    # left >= right 재귀 종료 같다는 조건이 있으면 안된다.
    if left > right: # 같다는 조건이 있으면, 재귀에서 돌다가 이쪽으로 빠져나가게 됨.
        return -1, cnt
    
    # 재귀가 돌아가는 것
    else:
        mid = (left+right)//2
        cnt += 1
        if arr[mid] == target:
            return mid, cnt
        
        elif arr[mid] < target: # target 값이 더 클 때,
            return Binary_search_recur(mid+1, right, target)
        else: # target값이 더 작을때
            return Binary_search_recur(left, mid-1, target)

print(Binary_search_recur(0, len(arr)-1, 534))
# Binary Search 자체도 log N의 복잡도를 가진다. 분할 정복하는 것이기 때문에




# Heap_sort with lt,rt