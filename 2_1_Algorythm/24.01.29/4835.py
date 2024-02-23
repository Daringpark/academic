#import sys
#input = sys.stdin.readline

T = int(input())

for i in range(1, T+1) :
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_list = []
    for j in range(N-M+1) :
        sum_value = sum(num_list[j:M+j])
        sum_list.append(sum_value)
    diff = max(sum_list) - min(sum_list)
    print(f'#{i} {diff}')