import sys
input = sys.stdin.readline

### O(N)
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
for i in range(N):
    print(numbers[i])

### O(logN) 짜리로 정렬을 빠르게 할 수 있다.