# import sys
# input = sys.stdin.readline

N = int(input())

for i in range(1, N+1) :
    K = int(input())
    num_list = list(map(int, input().split()))
    max_value = num_list[0]
    min_value = num_list[0]
    for number in num_list :
        if number > max_value :
            max_value = number
        if number < min_value :
            min_value = number
    print(f'#{i} {max_value - min_value}')