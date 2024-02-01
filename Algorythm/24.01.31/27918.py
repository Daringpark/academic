import sys
sys.stdin = open('27918.txt', 'r')

N = int(input())

Dcnt = Pcnt = 0
for i in range(N):
    player = input()
    if player == 'D' :
        Dcnt += 1
    else :
        Pcnt += 1
    diff = Dcnt - Pcnt
    if diff > 1 or diff < -1:
        break
print(f'{Dcnt}:{Pcnt}')
