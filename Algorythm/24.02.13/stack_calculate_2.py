# 괄호가 없는 계산 처리
prio = {'/':2, '*':2, '-':1, '+':1}

# fx = '2+3*4/5'
# fx = '3*1-4+2+8/4'
fx = '1-2+8/4-3*2+3'
result = ''

stack = []
for token in fx:
    if token.isdigit():
        result += token
    else:
        if stack and prio[token] > prio[stack[-1]]:
            stack.append(token)
        else:
            while stack and prio[token] <= prio[stack[-1]]:
                result += stack.pop()
            stack.append(token)

while stack:
    result += stack.pop()
print(result)

def cal(v1, v2, oper):
    if oper == '+':
        return int(v1) + int(v2)
    elif oper == '-':
        return int(v1) - int(v2)
    elif oper == '*':
        return int(v1) * int(v2)
    else: return int(v1) / int(v2)

stack2 = []
def step2():
    global result
    for token in result:
        if token.isdigit():
            stack2.append(token)
        else:
            v1 = stack2.pop()
            v2 = stack2.pop()
            stack2.append(cal(v2,v1,token))
    return stack2[0]
print(step2())