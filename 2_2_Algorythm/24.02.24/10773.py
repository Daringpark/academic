
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
    else :
        if Recepit:
            Recepit.pop()
print(sum(Recepit))