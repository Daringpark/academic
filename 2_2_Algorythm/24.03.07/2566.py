
N = 9
Matrix = [list(map(int, input().split())) for _ in range(N)]
max_value = -1
pos = []
for i in range(N):
    for j in range(N):
        if max_value < Matrix[i][j]:
            max_value = Matrix[i][j]
            pos = [i+1 , j+1]

print(max_value)
print(*pos)