import sys
input = sys.stdin.readline
def solve():
    global top
    if n == 2: # pop
        if top >= 0:
            print(stack.pop(top))
            top -= 1
        else:
            print(-1)
    elif n == 3: # size
        print(len(stack))
    elif n == 4: # isempty
        if stack:
            print(0)
        else:
            print(1)
    else: #top
        if stack:
            print(stack[top])
        else: print(-1)
N = int(input())
stack = []
top = -1
for i in range(N):
    order = input()
    if order[0] != '1':
        n = int(order)
        solve()
    else:
        n = list(map(int, order.split()))
        stack.append(n[1])
        top += 1


import sys
inputs = sys.stdin.readlines()
stk = list()
ans = list()
for i in range(1, len(inputs)):
    if inputs[i][0] == "1":
        stk.append(inputs[i].split()[1])
    elif inputs[i][0] == "2":
        if len(stk) > 0:
            ans.append(stk.pop())
        else:
            ans.append("-1")
    elif inputs[i][0] == "3":
        ans.append(str(len(stk)))
    elif inputs[i][0] == "4":
        if len(stk) > 0:
            ans.append("0")
        else:
            ans.append("1")
    elif inputs[i][0] == "5":
        if len(stk) > 0:
            ans.append(stk[-1])
        else:
            ans.append("-1")

print("\n".join(ans))