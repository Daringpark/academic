# 병합 정렬 알고리즘 코드 # 재귀 구현

def merge(lst1, lst2):
    result = []
    
    while len(lst1) > 0 or len(lst2) > 0 :
        if len(lst1) >0 and len(lst2) > 0:
            if lst1[0] <= lst2[0]:
                result.append(lst1.pop(0))
            else:
                result.append(lst2.pop(0))
        elif len(lst1) > 0:
            result.append(lst1.pop(0))
        elif len(lst2) > 0:
            result.append(lst2.pop(0))
    return result

def merge_sort(lst):
    
    if len(lst) == 1:
        return lst
    
    # 함수 내에서 좌, 우 리스트를 만들어서 넣어준다.
    left = []
    right = []
    # 중간 값 
    if len(lst)%2:
        half = (len(lst)-1)//2 # N-1//2 >> 7이면, 3
    else:
        half = len(lst)//2 # N//2 >> 8이면, 4 (0 1 2 3)
    
    for i in range(half): # 0 1 2
        left.append(lst[i])
    for j in range(half, len(lst)):
        right.append(lst[j])
    
    # 재귀를 통해서 정렬할 수 있음
    left = merge_sort(left) # 그 동안의 result는 left와 right으로 쪼개진다.
    right = merge_sort(right)

    # 정렬이 다 끝나면, 
    return merge(left, right) # return을 통해서 최종 출력을 할 수 있음


M = [254,54,76,125,69,75,31,2,99] # 9개
L = [54,76,125,69,75,31,2,99] # 8개


print(merge_sort(M))
print(sorted(M))

print(merge_sort(L))
print(sorted(L))