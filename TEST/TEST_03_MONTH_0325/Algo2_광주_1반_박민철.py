'''
4
3 35
11 10 19
4 826
559 281 278 27
5 572
88 255 570 839 39
25 100
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 99 45 44 24 10
> 1 * 20 + 45 24 12
= 20 45 24 10 = 99
= 20 44 24 10 = 98
'''
## N = 6 , limit 101
# 20 100 78 77 3 1

## 3 99
# 101001
# 20 78 1


## 4 101
# 100111
# 20 77 3 1

# 오답
# 4 99 # 각각 따로 간 경우, minV = min(minV)

# 정답
# cnt(level 끝까지 도달했을때, 우리가 취했던 1들 중 가장 높은 수) >> 4 101

# 그냥 최대한 많은 다리를 놓는것, 연결성을 따지고 그런건 아닌 것 같다.
# 그래프라기에는 부분집합 문제인 것 같음. C의 크기에 따라서 성능이 조금 달라질 수 있을 것 같다.
def back(n, s, cnt):
    global min_value, max_value

    if s > limit: # 예산을 넘어가게 된다면, 의미 없는 케이스임으로 그 케이스는 제외하고 부분집합 한다.
        return
    
    if n == N: # 건설 비용 한계 limit에 도달하지 않고 다 취했을 때를 의미함.
        if max_value < cnt: 
            min_value = s
            max_value = cnt
        elif max_value == cnt: # 더 적은 쪽을 택한다.
            min_value = min(min_value, s)
        return

    # 1, 0 > 2**N
    back(n+1, s + bridges[n], cnt+1)
    back(n+1, s, cnt)

T = int(input())
for tc in range(1, T+1):
    N, limit = map(int, input().split())
    bridges = list(map(int, input().split()))
    max_value = 0 # 최대 다리수는 0 이상일 것이다.
    min_value = limit
    back(0, 0, 0)
    print(f'#{tc} {max_value} {min_value}')