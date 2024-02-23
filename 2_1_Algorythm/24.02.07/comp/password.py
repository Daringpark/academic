import sys
sys.stdin = open('password.txt')

for tc in range(1, 11):
    N, raw_data = input().split()
    stack1 = [i for i in raw_data]
    stack2 = []
    N = int(N)
    for i in range(N):
        stack2.append(stack1.pop())
        if len(stack2) >= 2 and stack2[-1] == stack2[-2]:
            stack2.pop()
            stack2.pop()
    stack2.reverse()
    res = ''.join(stack2)
    print(f'#{tc} {res}')