
# import sys
# sys.stdout = open("output.txt", 'w')

T = int(input())
for tc in range(T):
    k = int(input()) # row
    n = int(input()) # col
    if k == 0:
        print(n)
    else:
        floor = [i for i in range(1, n+1)] # zero to goal floor
        for _ in range(k):
            for i in range(1, n):
                floor[i] += floor[i-1]
        print(floor[-1])

    