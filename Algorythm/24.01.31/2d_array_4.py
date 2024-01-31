import sys
sys.stdin = open('input_p4.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)

