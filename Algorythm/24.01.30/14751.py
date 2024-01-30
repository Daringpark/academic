import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input()) 
    lst = list(map(int, input()))
    zero_nine = [0] * 10

    # for idx in range(N): # sort
    #     for jdx in range(idx+1, N):
    #         if lst[idx] < lst[jdx] :
    #             lst[idx], lst[jdx] = lst[jdx], lst[idx]

    # for number in lst: # N을 사용하지 않은 경우
    #     zero_nine[number] += 1
    
    for idx in range(N): # N을 필수적으로 사용한 경우
        zero_nine[lst[idx]] += 1




    amount = 0
    for i in range(len(zero_nine)) :
        if zero_nine[i] == max(zero_nine) :
            max_value = i
            amount = zero_nine[i]

    print(f'#{test_case} {max_value} {amount}')