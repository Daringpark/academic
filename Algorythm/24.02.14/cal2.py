import sys
sys.stdin = open('cal2.txt')

def make(): # 후위 표기식
    global fx
    fx1 = ''
    top = -1
    stack = []
    for token in fx:
        if token.isdigit(): # 숫자는 계속 넣어준다.
            fx1 += token
        else: # operator coming
            if stack and pror[token] <= pror[stack[top]]:
                while stack and stack[top] != '+': # 최적 작성이 필요함
                    fx1 += stack.pop()
                    top -= 1
            stack.append(token)
            top += 1
    while stack:
        fx1 += stack.pop()
        top -= 1
    return fx1
def cal(a, b, oper):
    if oper == '+':
        return b + a
    else:
        return b * a
def solve(f):
    stack = []
    for token in f:
        if token.isdigit():
            stack.append(token)
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(cal(num1, num2, token))
    return stack[0]
pror = {'*': 2, '+': 1}
for tc in range(1, 11):
    N = int(input())
    fx = input()
    print(f'#{tc} {solve(make())}')