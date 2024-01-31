import sys
sys.stdin = open('2563.txt', 'r')

N = int(input())
space = [[0] * 100 for j in range(100)]
length = 10
for paper in range(N):
    s, e = map(int, input().split())
    for i in range(s, s+10):
        for j in range(e, e+10):
            space[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if space[i][j] == 1:
            cnt += 1
print(cnt)