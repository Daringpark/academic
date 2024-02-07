import sys
sys.stdin = open('input_4866.txt')

T = int(input())
for tc in range(1, T+1):
    stack1 = list(input())
    stack2 = []
    for i in range(len(stack1)):
        item = stack1.pop()
        if item == '{' or item == '}' or item == '(' or item == ')':
            stack2.append(item)
            if '}' in stack2:
                if stack2[-1] == '{':
                    stack2.pop()
                    stack2.pop() # 후입 선출하려면 같은 쌍으로 떨어져야 함. 결국 pop 두번
            if ')' in stack2:
                if stack2[-1] == '(':
                    stack2.pop()
                    stack2.pop()
    if stack2: res = 0
    else: res = 1
    print(f'#{tc} {res}') # ex) {(})의 경우, 0