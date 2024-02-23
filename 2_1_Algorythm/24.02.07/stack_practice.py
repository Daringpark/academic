import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    stack1 = list(input())
    stack2 = []
    size = len(stack1) # 필요한가?
    for i in stack1[::-1]:
        stack2.append(i)
        if ')' in stack2 and '(' in stack2: # 닫는 브라켓부터
            stack2.pop(stack2.index(')'))
            stack2.pop(stack2.index('('))

    if stack2:
        print(f'#{tc} 0')
        print(stack2)
    else:
        print(f'#{tc} 1')