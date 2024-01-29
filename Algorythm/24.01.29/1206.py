import sys
sys.stdin = open("input.txt", "r")

for T in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    res = 0
    for i in range(2, N-2): # 2에서 N-2까지의 값만 받으려고 함
        compare_list = lst[i-2 : i+3] # i-2, i-1, i, i+1, i+2
        max_value = max(compare_list) # 움직여가면서 5개의 max값을 비교
        if lst[i] == max_value: # 5개에서 max값이 i번째일때, 
            second_value = compare_list[0] # 일단 값 하나를 받아서, second_value에 넣어둠
            for j in range(5) : # 값을 비교하기 위해서 compare_list의 수를 비교하려함.
                if second_value < compare_list[j] < max_value : #second_value랑 max_value 사이에 있을 때, 
                    second_value = compare_list[j] # second_value를 갱신하기 위해서
            res += max_value - second_value # max_value - second_value를 res값으로 받기 # 추가적인 값이 생김
    print(f'#{T+1} {res}')

# 0 1 3 4 를 min