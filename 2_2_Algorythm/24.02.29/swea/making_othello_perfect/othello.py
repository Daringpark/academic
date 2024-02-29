









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

def checker_flip(lst):
    if lst:
        for i in lst: # 뒤집을 것들의 개수 [new_row, new_col]
            if board[i[0]][i[1]] == 1:
                board[i[0]][i[1]] = 2
            elif board[i[0]][i[1]] == 2:
                board[i[0]][i[1]] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 4 6 8
    board = [[0] * N for _ in range(N)]
    # 기존 세팅 4개 깔고 시작
    board[N//2-1][N//2-1] = board[N//2][N//2] = 2 # 백돌 세팅
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1 # 흑돌 세팅

    # 2 3 (입력) > 2 1 (배열)
    for _ in range(M): # 직접 보드에 체커를 놓는다. # 1은 흑돌, 2는 백돌
        col, row, color = map(int, input().split())
        col -= 1
        row -= 1
        board[row][col] = color # 체커를 놓은 시점
        # 적 체커를 비교하자.
        if color == 1:
            color_r = 2
        elif color == 2:
            color_r = 1

        my_change_checker = []
        for drdc in [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]: # 8방향을 탐색할겁니다.
            new_row = row + drdc[0]
            new_col = col + drdc[1]

            # direction = []
            # if 0 <= new_row < N and 0 <= new_col < N:
            # # 범위 안에 있으면서, 값이 있으면서(check가 놓여있는 경우), 값이 다를때 (check 색이 다를때) 방향을 저장하자.
            #     direction.append(drdc)
            # # 그럼 거기서부터 시작해서 같은 방향으로 색이 같은게 나올때까지 결정하고 뒤집자.
            # if direction: # 방향을 고를 수 있다면!
            #     print(direction)
            temp_check = [] # drdc
            idx = 1
            if 0 <= new_row < N and 0 <= new_col < N: # 바운더리 안에 있는지
                while board[new_row][new_col] and board[new_row][new_col] == color_r: # 0이 아닌가? + 그럼 그 값이 다른가까지
                    temp_check.append([new_row, new_col])
                    idx += 1
                    new_row = row + drdc[0] * idx
                    new_col = col + drdc[1] * idx
                    if not (0 <= new_row < N and 0 <= new_col < N):
                        temp_check = []
                        break
            # my_change_checker.extend(temp_check)
                    # if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] != color_r:
                    #     temp_check.append([new_row, new_col])
                    # elif : # 체커 엣지에서 다른 값을 찾지 못했을 경우,
                    #     temp_check = []

                # if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col]:
                #     while board[new_row][new_col] != color: # 같은 색을 만났을때,
                #         my_change_checker.append([new_row,new_col])
                #         idx += 1
                #         new_row = row + k[0] *idx
                #         new_col = col + k[1] *idx
                # if not (0 <= new_row < N and 0 <= new_col < N):
                #     my_change_checker = []
                #     break
                my_change_checker.extend(temp_check)
        checker_flip(my_change_checker)
        for i in range(N):
            print(*board[i])
        print()
    # 8 방향에 대해서 탐색 # 1은 2를 보고, 2는 1을 보고
    # 값 비교를 해보자. 2 1 2
    # 뒤집을 수 있겠다? 뒤집어보자.. (뒤집으면서 보면 안된다.)
    # for i in range(N):
    #     print(*board[i])
    print(f'#{tc} {checker_check()}')