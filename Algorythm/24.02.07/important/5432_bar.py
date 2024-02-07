import sys
sys.stdin = open('5432.txt')


T = int(input())

for tc in range(1, T+1):
    stack1 = list(input())
    stack2 = []
    N = len(stack1)
    cnt = 0
    length = 0
    for i in range(N):
        stack2.append(stack1.pop())
        if stack2[-1] == ')':
            length += 1
        else:
            length -= 1
            stack2.pop()
            stack2.pop()
            cnt += length

    print(f'#{tc} {cnt}')





