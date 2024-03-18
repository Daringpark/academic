# 병합 정렬 알고리즘 코드 # 재귀 구현

def merge(lst1, lst2):
    result = []
    lp = 0
    rp = 0
    while len(lst1) > lp and len(lst2) > rp: # 한 리스트가 끝까지 도달 했을 경우
        if lst1[lp] < lst2[rp]:
            result.append(lst1[lp])
            lp += 1
        else: # lst1[lp] > lst2[rp]
            result.append(lst2[rp])
            rp += 1
    # 남아있는 리스트를 넣어주기
    result.extend(lst1[lp:])
    result.extend(lst2[rp:])
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    # 중간 값 
    if len(lst)%2:
        half = int((len(lst)-1)/2) # N-1//2 >> 7이면, 3
    else:
        half = int(len(lst)/2) # N//2 >> 8이면, 4 (0 1 2 3)
    
    # 함수 내에서 좌, 우 리스트를 만들어서 넣어준다.
    # 재귀를 통해서 정렬할 수 있음
    left = merge_sort(lst[:half]) # 그 동안의 result는 left와 right으로 쪼개진다.
    right = merge_sort(lst[half:])
    # 정렬이 다 끝나면
    return merge(left, right) # return을 통해서 최종 출력을 할 수 있음

M = [254,54,76,125,69,75,31,2,99] # 9개
L = [54,76,125,69,75,31,2,99] # 8개

print(merge_sort(M))
print(sorted(M))

print(merge_sort(L))
print(sorted(L))
