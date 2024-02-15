def solve():
    for _ in range(M):
        item = numbers.pop(0)
        numbers.append(item)
    return numbers[0]

T = int(input())
for tc in range(1, T+1):
    N , M = map(int, input().split()) # N개의 숫자와 M개의 시행
    numbers = list(map(int, input().split()))
    print(f'#{tc} {solve()}')