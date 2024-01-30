import sys
sys.stdin = open("input.txt", "r")

for T in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    res = 0
    for i in range(2, N-2): # 2에서 N-2까지의 값만 받으려고 함
        compare_list = list((lst[i-2], lst[i-1], lst[i+1], lst[i+2])) # i를 기준으로 비교하고자 하는 값을 list로 받음
        max_value = max(compare_list) # 그 중 제일 큰 값을 뽑음
        if lst[i] > max_value: #  i번째 lst가 비교하는 것들 중 높은 값보다 클 때만 추가
            res += lst[i] - max_value # 그 단차만 res 변수에 추가
    print(f'#{T+1} {res}') # test_case가 끝날때마다 출력
