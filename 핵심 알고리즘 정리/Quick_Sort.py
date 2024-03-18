# Hoare-partition Algorythm
def partition_H(start, end):
    p = start
    i = start
    j = end
    while i <= j: # i보다 j가 클 때 break
        while i <= j and numbers[i] <= numbers[p]:
            i += 1
        while i <= j and numbers[j] >= numbers[p]:
            j -= 1
        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
    numbers[p], numbers[j] = numbers[j], numbers[p]
    return j

# Lomuto-partition Algorythm
def partition_l(start, end):
    p = end # pivot
    i = start-1 # 처음부터 탐색할 것
    
    for j in range(start, end): # 
        if numbers[j] < numbers[p]:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
        
    numbers[i+1], numbers[p] = numbers[p], numbers[i+1]
    return i+1

def quick_sort(left, right):
    if left < right:
        # Hoare-partition Algorythm
        # M = partition_H(left, right)
        
        M = partition_l(left, right)
        
        # 파티션을 기준으로 왼쪽은 작은 값, 오른쪽은 큰 값

        # 파티션을 기준으로 왼쪽과 오른쪽을 정렬한다
        quick_sort(left, M-1)
        quick_sort(M+1, right)

numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
N = len(numbers)
print(numbers)
quick_sort(0, N-1) # 인덱스를 기준으로
print(numbers)


### 펌
def quickSort(array, startIndex, endIndex):
    # verify that the start and end index have not overlapped
    if (startIndex < endIndex):
        # calculate the pivotIndex
        pivotIndex = partition(array, startIndex, endIndex)
        # sort the left sub-array
        quickSort(array, startIndex, pivotIndex)
        # sort the right sub-array
        quickSort(array, pivotIndex + 1, endIndex)

def partition(array, startIndex, endIndex):
    pivotIndex = (startIndex + endIndex) / 2
    pivotValue = array[int(pivotIndex)]

    while (True):

        # start at the FIRST index of the sub-array and increment
        # FORWARD until we find a value that is > pivotValue
        while (array[startIndex] < pivotValue): startIndex += 1

        # start at the LAST index of the sub-array and increment
        # BACKWARD until we find a value that is < pivotValue
        while (array[endIndex] > pivotValue): endIndex -= 1

        if (startIndex >= endIndex): return endIndex

        # swap values at the startIndex and endIndex
        temp = array[startIndex]
        array[startIndex] = array[endIndex]
        array[endIndex] = temp

if __name__ == '__main__':
    array = [12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8]
    quickSort(array, 0, len(array) - 1)
    print(array)