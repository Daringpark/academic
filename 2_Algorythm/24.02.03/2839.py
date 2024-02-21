import sys
sys.stdin = open('2839.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 옮겨야 할 설탕 무게
    lst = []
    for i in range(N//5, -1, -1):
        X = N - 5*i
        A = X % 3
        if A == 0 :
            lst.append(i + X//3)
    if lst:
        print(min(lst))
    else:
        print(-1)