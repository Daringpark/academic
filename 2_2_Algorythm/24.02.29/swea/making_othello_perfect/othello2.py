import sys
sys.stdin = open("othello.txt")

def checker_check():
    black = 0
    white = 0
    for i in range(N):
        if 1 in board[i]:
            black += board[i].count(1)
        if 2 in board[i]:
            white += board[i].count(2)
    return f'{black} {white}'
T = int(input())
for tc in range(1, T+ 1):
    N, M = map(int, input().split())  # 4 6 8
    board = [[0] * N for _ in range(N)]
    # 기존 세팅 4개 깔고 시작
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2  # 백돌 세팅
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1  # 흑돌 세팅
    # 2 3 (입력) > 2 1 (배열)
    for _ in range(M):  # 직접 보드에 체커를 놓는다. # 1은 흑돌, 2는 백돌
        col, row, color = map(int, input().split())
        col -= 1
        row -= 1
        board[row][col] = color  # 체커를 놓은 시점
        # 적 체커를 비교하자.
        if color == 1:
            color_r = 2
        elif color == 2:
            color_r = 1
        for drdc in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]:  # 8방향을 탐색할겁니다.
            new_row = row + drdc[0]
            new_col = col + drdc[1]
            temp_check = []  # drdc
            while 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == color_r:
                temp_check.append([new_row, new_col])
                new_row += drdc[0] # idx 없이 drdc의 값을 그대로 받아서 +=
                new_col += drdc[1]
                if 0 <= new_row < N and 0 <= new_col < N:
                    if board[new_row][new_col] == color:
                        for x, y in temp_check:
                            board[x][y] = color
        # for i in range(N):
        #     print(*board[i])
        # print()
    print(f'#{tc} {checker_check()}')