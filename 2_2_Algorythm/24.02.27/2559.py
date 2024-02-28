
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]
max_value = prefix_sum[K]
# 구간의 합을 이용하여 최대 합을 구합니다.
for i in range(N - K + 1):
    sum_value = prefix_sum[i + K] - prefix_sum[i]
    if max_value < sum_value:
        max_value = sum_value
print(max_value)