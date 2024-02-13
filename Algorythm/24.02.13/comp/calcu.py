import sys
sys.stdin = open('cal_input.txt')

def make(): # 후위식 생성 함수
    fx1 = '' # 붙혀줘야할 새로운 후위 방정식
    for token in fx:
        if token == '+':
            stack.append(token)
        else : fx1 += token
        # stack과 숫자를 잘 배열해서 새로운 후위 방정식을 정리해서 반환
        while stack and token != '+':
            fx1 += stack.pop()
    return fx1

def solve(fx): # 후위식 풀이 함수
    for token in fx:
        if token != '+':
            stack2.append(token)
        elif stack2 and token == '+':
            v2 = int(stack2.pop())
            v1 = int(stack2.pop())
            stack2.append(v1+v2)
    result = stack2[0]
    return result  # 최종 합을 출력

for tc in range(1, 11):
    N = int(input()) # 초기 표기식의 길이
    fx = input() # N 길이의 중위 표기식
    stack = []  # operator 넣고 뺄 곳
    stack2 = []  # number 넣을 곳

    print(f'#{tc} {solve(make())}') # 후위 방정식 구한 이후, 방정식 풀이