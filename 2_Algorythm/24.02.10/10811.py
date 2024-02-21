import sys
sys.stdin = open('10811.txt', 'r')

N, M = map(int, input().split())
bucket = [i for i in range(1, N+1)]

for i in range(M):
    start, end = map(int, input().split())
    for j in range((end-start+1)//2):
        bucket[start+j-1], bucket[end-j-1] = bucket[end-j-1], bucket[start+j-1]
result = ' '.join(map(str, bucket))
print(result)