'''
5 16
1 3 3 5 6
'''

# 부분집합 문제네
def back(n, s): # 재귀식으로 풀어보고자 한다.
    global min_value, cnt

    # 기저 조건 만들기
    # 먼저 확인해야하는 기저 조건
    # "현재까지" s가 limit을 넘어 갔을때, s >= limit
    if s >= limit :
        min_value = min(s, min_value)
        return
    
    # "현재까지" 점원을 다 뽑았을 때, n == N
    if n == N:
        return

    # 그럼 이제 이 부분에서 재귀를 돌려보자.
    # 2 ** N
    
    # 쌓는다면,
    back(n+1, s+people[n]) # 1
    # 안 쌓는다면,
    back(n+1, s) # 0

T = int(input())
for tc in range(1, T+1):
    N, limit = map(int, input().split()) # 5 16
    people = list(map(int, input().split()))
    min_value = 3*1e5 # 각 점원의 키는 1e4 * N은 20 이하..

    cnt = 0
    # 처음 결과 값은 0 + subsum 추가
    back(0, 0)
    print(f'#{tc} {abs(min_value - limit)}')