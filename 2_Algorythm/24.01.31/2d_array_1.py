# 3
# 1 2 3
# 4 5 6
# 7 8 9
import sys
sys.stdin = open('input_p1.txt', 'r')

N = int(input())
arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))
arr = [list(map(int, input().split())) for _ in range(N)] # list comprehension
arr2 = [[0]*N for _ in range(N)]
arr3 = [[0]*N]*N # shallow copy
print(arr)
print(arr2)
print(arr3)
# 배열 순회 : 행, 열 우선 순회
def f(*args):
    print(*args)

for i in range(N): # i열을 고정하면서 j행을 먼저 처리한다. (가로 방향)
    for j in range(N):
        f(arr[i][j])
        arr[i][j] = 0
        print(arr)
for i in range(N): # j행을 고정하면서 i열을 먼저 처리한다. (세로 방향)
    for j in range(N):
        f(arr[j][i]) # 이 경우, 정사각형 행렬이 아닐 경우, 충돌
        arr[j][i] = 1
        print(arr)