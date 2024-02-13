icp ={')': 0, '*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp ={'(': 0, '*': 2, '/': 2, '+': 1, '-': 1, ')': 3}

fx = '(6+5*(2-8)/2)'
result = ''

stack = [0]*10
top = -1
for token in fx:
    # push의 경우, top위치에 token을 추가 top += 1
    if token == '(' or (token in '*+-/' and isp[stack[top]] < icp[token]):
        top += 1
        stack[top] = token
    elif token in '*+-/' and isp[stack[top]] >= icp[token]:
        while isp[stack[top]] >= icp[token]:
            top -= 1
            result += stack[top+1]
        top += 1
        result += stack[top+1]
    elif token == ')':
        while stack[top] != '(':
            top -= 1
            result += stack[top+1]
            # stack[top + 1] = 0
        top -= 1
        # stack[top+1] = 0
    else: result += token
print(result)