import sys
sys.stdin = open('10103.txt', 'r')

A = 100
B = 100
N = int(input())

for i in range(N):
    X, Y = map(int, input().split())
    if X > Y :
        B -= X
    elif X < Y :
        A -= Y
    else :
        pass

print(f'{A}\n{B}')