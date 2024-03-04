
# 1을 체크해야함.
N = int(input())
max_n = 0
max_res = []
for i in range(1, N+1):
    res = [N]
    X = N
    x = i # 두 번째 숫자
    res.append(x)
    n = 2 # 카운트
    while X-x >= 0 :
        res.append(X-x)
        n += 1
        X = res[-2]
        x = res[-1]
        
    if n > max_n:
        max_n = n
        max_res = res
print(max_n)
print(*max_res)