import sys
sys.stdin = open('input_pendi1.txt')

def row_max(n):
    for i in range(100):
        for j in range(100-n+1):
            flag = 1
            for k in range(n//2):
                if space[i][j+k] != space[i][j+n-1-k]: # 여기서 바로 걸리네
                    flag = 0
                    break
            if flag:
                return j

def col_max(n):
    for i in range(100):
        for j in range(100-n+1):
            flag = 1
            for k in range(n//2):
                if space[j+k][i] != space[j+n-1-k][i]:
                    flag = 0
                    break
            if flag:
                return j

for tc in range(1, 11):
    N = int(input()) #문제 번호
    space = [input() for _ in range(8)]

    cnt = 0
    for i in range(100, 1, -1):
        if row_max(i) > col_max(i):
            cnt = row_max(i)
        else :
            cnt = col_max(i)
    else :
        cnt = 1

    print(f'#{tc} {cnt}') 