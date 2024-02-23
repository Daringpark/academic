import sys
sys.stdin = open("5186.txt")
def solve():
    global N
    res = ''
    k = 0.5
    while N != 0.0: # 12일때 탈출하게 된다.
        if N >= k:
            N -= k
            k /= 2
            res += '1'
        else:
            k /= 2
            res += '0'
        if len(res) >= 13:
            return f'overflow'
    return res
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {solve()}')