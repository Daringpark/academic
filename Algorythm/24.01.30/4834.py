import sys
sys.stdin = open("input_4834.txt", "r")

# 선택 정렬 // 제자리 정렬
# for idx in range(N): # sort
#     for jdx in range(idx+1, N):
#         if lst[idx] < lst[jdx] :
#             lst[idx], lst[jdx] = lst[jdx], lst[idx]

# Bubble Sort
T = int(input())
def max_lst(lst):
    max_lst_value = lst[0]
    for number in lst:
        if number > max_lst_value:
            max_lst_value = number

for test_case in range(1, T+1):
    N = int(input()) 
    lst = list(map(int, input()))
    cnt_lst = [0] * 10 # count_list를 만들어준다.

    # 첫 번째 카운트 업
    for idx in range(N): # N을 필수적으로 사용한 경우
        cnt_lst[lst[idx]] += 1 # 0번부터 N-1번까지의 lst의 수를 cnt_lst 인덱스에 카운팅
    # for number in lst: # N을 사용하지 않은 경우 복잡도는 O(N) 동일
    #     zero_nine[number] += 1

    amount = 0
    max_value = None
    for i in range(10) : # cnt_list의 0~9까지의 카운팅 인덱스를 가져오려고
        if cnt_lst[i] == max_lst(cnt_lst) :
            max_value = i
            amount = cnt_lst[i]

    print(f'#{test_case} {max_value} {amount}')