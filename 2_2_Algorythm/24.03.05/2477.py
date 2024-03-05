
# 참외밭

'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''

import sys
input = sys.stdin.readline

stack = []
N = int(input()) # 1 제곱평방미터에서 자라는 참외의 개수
for i in range(6): # 6번의 입력을 받을 예정
# 1,2는 동, 서 (가로 방향); 3,4는 남, 북 (세로 방향)
    direction, amount = map(int, input().split())
    stack.append([direction, amount])
stack = stack * 2

for i in range(6):
    if stack[i][0] == stack[i+2][0] and stack[i+1][0] == stack[i+3][0]:
        m_1 = stack[i+1][1]
        m_2 = stack[i+2][1]
        M_1 = stack[i+4][1]
        M_2 = stack[i+5][1]
        break
print(N*((M_1*M_2)-(m_1*m_2)))