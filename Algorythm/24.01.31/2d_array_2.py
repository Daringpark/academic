import sys
sys.stdin = open('input_p2.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def f(*args):
    print(*args)

# 지그재그 순회
for i in range(N):
    for j in range(M):
        f(arr[i][j + i%2 * (M-1-2*j)])
print(arr)