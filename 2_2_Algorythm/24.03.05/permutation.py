


# w + x + y + z = 10
N = 10
for w in range(1, N-2):
    for x in range(1, N-1):
        for y in range(1, N):
            z = N - (w + x + y)
            if z >= 1 and w + x + y + z == N:
                print(w, x, y, z)