'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
N = int(input())
E = N-1 # 간선 갯수
arr = list(map(int, input().split()))
left = [0] * (N+1)
right = [0] * (N+1)
par = [0] * (N+1)

def pre_order(T):
    if T :
        print(T, end = ' ') # VLR
        pre_order(left[T])
        pre_order(right[T])

def in_order(T):
    if T :
        in_order(left[T])
        print(T, end = ' ') # VLR
        in_order(right[T])

for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0:
    c = par[c]
root = c
print(root)
print(left)
print(right)
print(par)
pre_order(root)
print()
in_order(root)