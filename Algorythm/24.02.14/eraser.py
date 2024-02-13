
N = int(input())
space = [i for i in range(1, N+1)]
n = len(space)
while n != 1:
    stack = []
    for i in range(n):
        if i%2:
            stack.append(space[i])
        else:
            pass
    if stack:
        space = stack
    n = len(space)
print(space[0])

