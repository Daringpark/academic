'''
5 16
1 3 3 5 6
'''

# 부분집합 문제네
def back(n, s):
    global min_value, cnt
    
    # 얘가 적당히 돌았을 때, 덜 적은것 과 비교하면 된다.
    # if abs(limit-s) > min_value:
        # return
    
    if n == N and s > limit:
        min_value = min(min_value, abs(limit-s))
        return
    
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            back(n+1, s+people[i])
            visited[i] = 0


N, limit = map(int, input().split()) # 5 16
people = list(map(int, input().split()))
visited = [0] * N
min_value = 2*1e5

cnt = 0
# 처음 결과 값은 0 + subsum 추가
back(0, 0)
print(min_value)
