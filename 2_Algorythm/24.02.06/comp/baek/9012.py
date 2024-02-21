import sys
input = sys.stdin.readline

N = int(input())

# 괄호 문자열의 길이는 50 이하
for _ in range(N):
    stackA = list(map(str, input().strip()))
    stackB = []
    
    for i in range(len(stackA)): # O(N)
        stackB.append(stackA.pop()) # append
        if ')' in stackB and '(' in stackB and stackB.index(')') < stackB.index('('):
            # remove method는 후입선출이 아닌 것 같은데
            stackB.remove('(')
            stackB.remove(')')

    if stackA or stackB:
        print('NO')
    else:
        print('YES')