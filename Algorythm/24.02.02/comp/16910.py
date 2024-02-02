import sys
sys.stdin = open('16910.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    radius = N = int(input())
    cnt = 0
    for x in range(-N, N+1): # 2차원 배열로 풀지 않았을 때
        for y in range(-N, N+1):
            if x**2 + y**2 <= N**2:
                cnt += 1
    print(f'#{tc} {cnt}')

### 원 안의 점을 2차원 배열을 사용해서 풀 수 있을까?