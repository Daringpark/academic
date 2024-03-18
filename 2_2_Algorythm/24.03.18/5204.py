
def merge(lst1, lst2):
    global cnt
    result = []
    # length 1 2 4 8 16 ...
    # pop해서 쓰거나 i ++ 쓰거나
    li = 0
    ri = 0
    if lst1[-1] > lst2[-1]:
        cnt += 1
    while len(lst1) > li and len(lst2) > ri: # li와 ri가 끝까지 도달할 때까지
        if lst1[li] < lst2[ri]: # left가 더 작을 경우, 오름차순 정렬
            result.append(lst1[li])
            li += 1
        else:
            result.append(lst2[ri])
            ri += 1
    result.extend(lst1[li:])
    result.extend(lst2[ri:])
    return result

def merge_sort(lst):
    # 재귀식
    if len(lst) == 1:
        return lst

    half = len(lst) // 2
    # 좌우로 나눠들어가는것
    left = merge_sort(lst[:half])
    right = merge_sort(lst[half:])
    result_list = merge(left, right)
    
    if len(lst) == N:
        return result_list[N//2]
    else:
        return result_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0 # 오른쪽 원소가 먼저 복사되는 경우
    number = 0 # sort이후에 N//2의 인덱스에 있는 값    
    print(f'#{tc} {merge_sort(numbers)} {cnt}')

# 2 2 1 1 3
# 1 1 2 2 3
# #1 2 0 (5//2 == 2번째)