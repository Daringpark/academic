
'''
1
8 3
0 0 0 0 0 1 0 0
0 1 0 1 0 0 0 1
0 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0
0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 1 0
1 0 0 0 0 0 0 0
'''

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split()) # matrix N*N 행렬, M = 가구당 낼 수 있는 price
    Matrix = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} ')
    for i in range(N):
        print(*Matrix[i])
    print()

## 서비스 영역은 길이가 K인 다이아몬드
# K = 3, 1 3 5 3 1 = 13
# K = 4, 1 3 5 7 5 3 1 = 25

# 초기 price값을 k = 1인 녀석으로 잡고,
## K+1의 price가 <= 그 앞선 price와 같거나 작으면 만들 필요 없다. >> 그럼 그 다다음 거의 이익이 많이난다면?

# 완전 탐색으로 모든 좌표의 값을 고려해야함.
# 해당 위치에서 집 위치와의 차이를 구한다...?
# 위치 차이가 가장 많은 집을 기준으로 K를 설정해서 프라이스로 받는다면. >> 프라이스 기준이 아니라 집 기준이 되버린다.
# 집 위치 차이의 최대값(K=10)을 기준으로 1~K(10) range(1, K+1) 인덱스를 고려해서


def home_check(row, col):
    pass

    # distance = []
    # for i in range(N):
    #     for j in range(N):




# 하나의 포지션에서 집들의 거리를 계산한다. 해서 나온게 distance
distance = [1,3,5,5,3,1,3,5,5,5,3,5]
example = dict()
our_max = max(distance)
for i in range(1, our_max+1): # 비어있는걸 고려한다면
    example[i] = 0
for k in distance:
    example[k] += 1
print(example)
M = 3
max_value = 0
pos = 0
for i in range(1, our_max+1):
    profit = example[i]*M - (i**2 + (i-1)**2)
    if max_value < profit:
        pos = i
print(f'{pos}가 제일 높은 값을 받습니다. 총 {example[pos]}개의 가정을 서비스합니다.') # k = 1일때 제일 가치가 높다.
example = {1 : 2, 3 : 4, 5: 6}
print(example)