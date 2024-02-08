import sys
sys.stdin = open('bubble.txt')

N = list(map(int, input().split()))
i = 0
while N != [1,2,3,4,5]:
    if N[i] > N[i+1]:
        N[i], N[i+1] = N[i+1], N[i]
        print(' '.join(list(map(str, N))))
    i += 1
    if i == 4:
        i = 0