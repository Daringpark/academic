import sys
sys.stdin = open('7568.txt', 'r')

N = int(input())

user_data = [list(map(int, input().split())) for _ in range(N)]
print(user_data[0][0])
# N <= 50
print(user_data)