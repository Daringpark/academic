import sys
sys.stdin = open("sleep.txt")

T = int(input())
for tc in range(1, T+1):
    count_list = [0] * 10 # visitied
    N = int(input()) # N번
    k = 1
    while sum(count_list) != 10:
        point = k*N
        res = point
        while point != 0:
            count_list[point%10] = 1
            point //= 10
        k += 1
    print(f'#{tc} {res}')