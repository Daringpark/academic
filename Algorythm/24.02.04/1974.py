import sys
sys.stdin = open('1974.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    row = 0
    col = 0
    block = 0
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            row_set.add(sudoku[i][j])
            col_set.add(sudoku[j][i])
        if len(row_set) == 9:
            row += 1
        if len(col_set) == 9:
            col += 1

    for row_start in range(0,9,3):
        for col_start in range(0,9,3):
            block_set = set()
            for i in range(3):
                for j in range(3):
                    block_set.add(sudoku[row_start+i][col_start+j])
            if len(block_set) == 9:
                block += 1

    if row == 9 and col == 9 and block == 9: res = 1
    else : res = 0

    print(f'#{tc} {res}')