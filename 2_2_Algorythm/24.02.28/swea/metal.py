
'''
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
'''
T = int(input())
for tc in range(1, T+1):
    metal = input()
    N = len(metal)
    cnt = 0
    total = 0
    for i in range(N): # 그 전 값과 비교해야하기 때문에 idx를 사용한다. # i <= N-1:
        if metal[i] == '(':
            cnt += 1
        elif metal[i] == ')':
            cnt -= 1
            if metal[i-1] == '(':
                total += cnt
            elif metal[i-1] == ')':
                total += 1

    print(f'#{tc} {total}')