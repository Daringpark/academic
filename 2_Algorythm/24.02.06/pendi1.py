import sys
sys.stdin = open('input_pendi1.txt')

def row_solve(n):
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            flag = 1
            for k in range(n//2):
                if space[i][j+k] != space[i][j+n-1-k]:
                    flag = 0
                    break
            if flag:
                cnt += 1
    return cnt
def col_solve(n):
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            flag = 1
            for k in range(n//2):
                if space[j+k][i] != space[j+n-1-k][i]:
                    flag = 0
                    break
            if flag:
                cnt += 1
    return cnt

for tc in range(1, 11):
    N = int(input())
    space = [input() for _ in range(8)]
    print(f'#{tc} {row_solve(N)+col_solve(N)}') 