L = int(input())
order = list(input())
x, y = 0, 0
memory = set()
memory.add((x,y))
def direction(n):
    global x, y
    if n == 'N':
        y += 1
    elif n == 'S':
        y += -1
    elif n == 'E':
        x += 1
    else:
        x += -1
    return (x,y)
def solve():
    for i in order:
        if direction(i) not in memory:
            memory.add(direction(i))
    return len(memory) 

print(solve())