import sys
sys.stdin = open('1974.txt', 'r')

T = int(input())
def vaild(lst, key):
    check = 0
    for i in range(len(lst)):
        if lst[i] == key:
            check += 1
    return check
def my_sum(lst):
    sum_value = 0
    for i in range(len(lst)):
        sum_value += lst[i]
    return sum_value

for tc in range(1, T+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]


    row_check = [0]*9
    # 행 확인
    for i in range(9): # 1,2,3,4,5,6,7,8,9
        row = []
        for j in range(1, 10):
            row.append(vaild(sudoku[i], j))
        if my_sum(row) == 9:
            row_check[i] = 1
        else :
            row_check[i] = 0

    col_check = [0]*9
    # 열을 리스트로 저장
    for i in range(9):
        new_col = []
        for j in range(9):
            new_col.append(sudoku[j][i])
    # print(new_col)
    # 열 확인
    for i in range(9): # 1,2,3,4,5,6,7,8,9
        col = []
        for j in range(1, 10):
            col.append(vaild(new_col, j))
        if my_sum(col) == 9:
            col_check[i] = 1
        else:
            col_check[i] = 0

    block_check = [1,2,4,2]

    if my_sum(row_check) == 9 and my_sum(col_check) == 9 and my_sum(block_check) == 9:
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')