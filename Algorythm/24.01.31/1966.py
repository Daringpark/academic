import sys
sys.stdin = open('1966.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            if numbers[i] < numbers[j]: # 선택 정렬하는 경우
                numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers = list(map(str, numbers))
    numbers = ' '.join(numbers)
    print(f'#{tc} {numbers}')