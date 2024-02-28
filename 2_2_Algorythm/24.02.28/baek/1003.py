


def zero_one_counts(numbers):
    if numbers >= 2:
        memo = [[0, 0] for _ in range(numbers+1)]
        memo[0] = [1, 0]
        memo[1] = [0, 1]
        for idx in range(2, numbers+1):
            memo[idx][0] = memo[idx-2][0] + memo[idx-1][0]
            memo[idx][1] = memo[idx-2][1] + memo[idx-1][1]
    if numbers == 1:
        return f'0 1'
    elif numbers == 0:
        return f'1 0'
    else:
        return f'{memo[numbers][0]} {memo[numbers][1]}'
N = int(input())
for _ in range(N):
    n = int(input()) # 해당 메모까지
    # 함수를 호출해서 저 두 변수에 호출된 값을 바꿔준다.
    print(zero_one_counts(n))