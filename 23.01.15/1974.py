# 스도쿠 문제풀이 알고리즘

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

#checklist

for test_case in range(T):
    X = []
    pre_box = []
    result = 0
    for i in range(9):
        x = list(map(int, input().split()))
        X.append(x)

    for m in range(3): #한줄씩 이동
        for n in range(3):
            A = [0]*9
            for k in range(9): #가로줄 확인
                a = X[m*3+n][k]
                A[a-1] += 1
            # print(A)
        
            B = [0]*9
            for l in range(9):  #세로줄 확인
                b = X[l][m*3+n]
                B[b-1] += 1
            # print(B)

            C = [0]*9
            for o in range(3):   #3*3정사각형 확인
                for p in range(3):
                    c = X[p+n*3][o+m*3]
                    C[c-1] += 1
            # print(C)
                    
        #check function
            if (A.count(1) == 9) and (B.count(1) == 9) and (C.count(1) == 9) :
                pre_box.append(1)
            else :
                pre_box.append(0)
    if sum(pre_box) == 9 :
        result = 1
    else :
        result = 0
    print(f'#{test_case+1} {result}')