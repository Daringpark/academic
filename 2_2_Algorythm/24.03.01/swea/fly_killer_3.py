
def solve():
    global max_value
    drdc = [[-1,0], [0,1], [1,0], [0,-1]]

    # 총 두 번 뿌려볼 생각이다.
    for row in range(N):
        for col in range(N): # 시작 좌표 받기
            plus_sum_value = Matrix[row][col]
            for i in range(1, M): # 0 1 2
                for flag in range(4):
                    new_row = row + drdc[flag][0] * i
                    new_col = col + drdc[flag][1] * i
                    if 0 <= new_row < N and 0 <= new_col < N:
                        plus_sum_value += Matrix[new_row][new_col]
            if plus_sum_value > max_value:
                max_value = plus_sum_value

            cross_sum_value = 0
            for i in range(-M+1, M):
                new_row = row + i
                new_col = col + i
                if 0 <= new_row < N and 0 <= new_col < N:
                    cross_sum_value += Matrix[new_row][new_col]

                new_row = row - i
                new_col = col + i
                if 0 <= new_row < N and 0 <= new_col < N:
                    cross_sum_value += Matrix[new_row][new_col]
                if i == 0: # 0 0 이 두개가 들어감
                    cross_sum_value -= Matrix[row][col]
            if cross_sum_value > max_value:
                max_value = cross_sum_value

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Matrix = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0
    solve()
    print(f'#{tc} {max_value}')


def kill(r, c, M):
    sum_1 = arr[r][c] # +분사의 합
    sum_2 = arr[r][c] # x분사의 합
    # +형태로 분사
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        for j in range(1, M):
            newR = r + dr[i]*j
            newC = c + dc[i]*j
            if 0<=newR<N and 0<=newC<N:
                sum_1 += arr[newR][newC]
    # X형태로 분사
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, 1, -1]
    for i in range(4):
        for j in range(1, M):
            newR = r + dr[i]*j
            newC = c + dc[i]*j
            if 0<=newR<N and 0<=newC<N:
                sum_2 += arr[newR][newC]
    # 둘중의 최대값 반환
    if sum_1 < sum_2:
        return sum_2
    else:
        return sum_1
 
 
T = int(input())
 
for tc in range(1,T+1):
    N, M = map(int, input().split())
    # NxN 배열 M : 분사 세기
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxX = 0
    for r in range(N):
        for c in range(N):
            sumX = kill(r,c,M)
            if maxX < sumX:
                maxX = sumX
 
    print(f'#{tc} {maxX}')