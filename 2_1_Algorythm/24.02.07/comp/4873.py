import sys
sys.stdin = open('input_4873.txt')

T = int(input())

for tc in range(1, T+1):

    stack1 = list(input())
    stack2 = []
    for _ in range(len(stack1)):
        if stack1:
            stack2.append(stack1.pop())
            if len(stack2) >= 2 and stack2[-1] == stack2[-2]:
                stack2.pop()
                stack2.pop()
    print(f'#{tc} {len(stack2)}')