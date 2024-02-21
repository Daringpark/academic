import sys
sys.stdin = open('input_1855.txt')
K = int(input()) # col = 3
word = input()
M = len(word) # 12
N = M//K # row
res = ''
space = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        space[i][j] = word[K*i+j]
    if i%2 == 1:
        space[i] = space[i][::-1]

for i in range(K): #col
    for j in range(N): #row
        res += space[j][i]

print(res)