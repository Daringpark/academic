

'''
5 4
.D.*
....
..X.
S.*.
....

4
'''

# 시간제한 1초
# N*M = 2500

# 물이 찰 예정인 칸에는 딛지 못한다.
# def flood():
    





# def move():






N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
# 비버 굴은 D, 고슴도치는 S
# S가 D에 도달할 수 없다면, KAKTUS
# *은 물이고, X는 돌

# 우선 탐색하고 나서, 
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'S':
            start = (i, j)
        if matrix[i][j] == 'D':
            end = (i, j)

print(start)
print(end)




for i in range(N):
    print(*matrix[i])