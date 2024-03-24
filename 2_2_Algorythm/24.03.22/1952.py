
# 완전탐색으로 풀이하자?
def dfs(m, c):
    global min_value
    # 기저 조건
    # 12월이면 종료
    if m == 12:
        min_value = min(min_value, c)
        return
    # 이미 최소값을 넘어갔다? 조기 종료
    if min_value < c or m > 12:
        return
    
    # 1일권을 구매할 경우
    dfs(m+1, c+months[m]*price[0])

    # 한 달권을 구매할 경우
    dfs(m+1, c+price[1])
    
    # 세 달권을 구매할 경우
    dfs(m+3, c+price[2])

T = int(input())
for tc in range(1, T+1):
    
    price = list(map(int, input().split()))
    months = list(map(int, input().split()))
    
    # 3000 * 30 * 12
    min_value  = int(1e7)
    dfs(0, 0) # start month 0 ~ 11
    # 1년권의 경우, 밖에서 생각해보자.
    min_value = min(price[-1], min_value)
    
    print(f'#{tc} {min_value}')