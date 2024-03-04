import sys
input = sys.stdin.readline

def min_operations(N):
    dp = [0] * (N + 1)  # dp[i]: 정수 i를 1로 만들기 위한 최소 연산 횟수
    sequence = [[] for _ in range(N + 1)]  # 각 정수에 대한 연산 순서를 저장

    for i in range(2, N + 1):
        # 1을 빼는 경우
        dp[i] = dp[i - 1] + 1
        sequence[i] = sequence[i - 1] + [i - 1]

        # 2로 나누어 떨어지는 경우
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            sequence[i] = sequence[i // 2] + [i // 2]

        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            sequence[i] = sequence[i // 3] + [i // 3]

    return dp[N], sequence[N]

N = int(input())
min_ops, ops_sequence = min_operations(N)
ops_sequence.append(N)
ops_sequence.reverse()
print(min_ops)
print(*ops_sequence)


#####
N = int(input())
dp = [N+1]*(N+1)
dp[1] = 0
prev = [0]*(N+1)
for i in range(2, N+1):
    if i%3==0 and dp[i//3]+1 < dp[i]:
        dp[i] = dp[i//3] + 1
        prev[i] = i//3
    if i%2==0 and dp[i//2]+1 < dp[i]:
        dp[i] = dp[i//2] + 1
        prev[i] = i//2
    if dp[i-1]+1 < dp[i]:
        dp[i] = dp[i-1] + 1
        prev[i] = i-1
print(dp[N])
print(N, end=' ')
i = N
while prev[i] != 0:
    i = prev[i]
    print(i, end=' ')