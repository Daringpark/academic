
N = int(input())

idx = 0
x = 1
while N > x :
    idx += 1
    x += 6 * idx
print(idx+1)