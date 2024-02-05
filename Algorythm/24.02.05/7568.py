import sys
sys.stdin = open('7568.txt', 'r')

N = int(input())

user_data = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):

    if user_data[i][0]