
# 10773 제로
import sys
sys.stdin = open("10773.txt")

import sys
input = sys.stdin.readline
K = int(input())
Recepit = []
for i in range(K):
    A = int(input())
    if A > 0:
        Recepit.append(A)
    else : # 0을 외치는 경우, 그 전의 값을 까먹게 된다!
        if Recepit:
            Recepit.pop()
print(sum(Recepit))