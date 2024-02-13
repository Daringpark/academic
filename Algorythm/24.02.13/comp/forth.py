import sys
sys.stdin = open('forth.txt')
def cal(op, a, b):
    if op == '+':
        return b + a
    elif op == '-':
        return b - a
    elif op == '*':
        return b * a
    else:
        return b//a # int

def solve(fx): # number를 저장하고, 연산식이 나왔을 경우, 연산자와 pop*2를 연산
    for token in fx:
        if token == '.': # stack2가 비어있을 경우, index error가 뜰 텐데!
            try:
                if len(stack2) < 2:
                    return stack2.pop()
                else: return f'error'
            except IndexError:
                return f'error'
        if token.isdigit():
            stack2.append(token)
        else :
            try:
                v2 = int(stack2.pop())
                v1 = int(stack2.pop()) # 연산 과정에서 맞지 않는 경우
                stack2.append(cal(token, v2, v1))
            except IndexError: return f'error'

T = int(input())
for tc in range(1, T+1):
    fx = list(input().split())
    stack2 = [] # number 저장
    print(f'#{tc} {solve(fx)}')
