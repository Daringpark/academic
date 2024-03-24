'''
5 16
1 3 3 5 6
'''

# 부분집합 문제네
def back(n, s): # 재귀식으로 풀어보고자 한다.
    global min_value, cnt
    
    # 백트래킹으로 하려고 한다? 많이 어려울 것이다...
    
    # 얘가 적당히 돌았을 때, 덜 적은것 과 비교하면 된다.
    if s > limit and abs(limit-s) > min_value:
        return
    
    if s > limit:
        min_value = min(min_value, abs(limit-s))
        return    
    
    if n == N:
        if s > limit:
            min_value = min(min_value, abs(limit-s))
        # 높이가 작은 경우는 그냥 무시해야 됨...
        return
    
    # permutation 해보자
    for i in range(N-1, -1, -1):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            back(n+1, s+people[i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, limit = map(int, input().split()) # 5 16
    people = list(map(int, input().split()))
    people.sort()
    visited = [0] * N
    min_value = 3*1e5 # 각 점원의 키는 1e4 * N은 20 이하..

    cnt = 0
    # 처음 결과 값은 0 + subsum 추가
    back(0, 0)
    print(f'#{tc} {min_value}')
    print(cnt)
