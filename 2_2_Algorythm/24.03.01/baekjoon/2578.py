
def solve(num):
    for row in range(5):
        for col in range(5):
            if Bingo_board[row][col] == number:
                Bingo_board[row][col] = 0 # 해당 넘버 체크하기
def check():
    three_cnt = 0

    for row in range(5):
        if Bingo_board[row].count(0) == 5: # bingo
            three_cnt += 1
        
        col_check = 0
        for col in range(5):
            if Bingo_board[col][row] == 0: # here col = row, row = col for rotate search
                col_check += 1
        if col_check == 5: # bingo
            three_cnt += 1
    
    cross_check_left = 0
    cross_check_right = 0
    for i in range(5): # crosscheck
        if Bingo_board[i][i] == 0:
            cross_check_left += 1
        if Bingo_board[i][4-i] == 0:
            cross_check_right += 1
    
    if cross_check_left == 5: # bingo
        three_cnt += 1
    
    if cross_check_right == 5: # bingo
        three_cnt += 1
    
    if three_cnt >= 3:
        return 1
    return 0

Bingo_board = [list(map(int, input().split())) for _ in range(5)]
order = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for numbers in order: # 한 개씩 부른다.
    for number in numbers:
        cnt += 1 # 부를 때 빙고가 나올 수 있기 때문에!
        solve(number)
        # cnt >= 5이상이면서, 빙고가 나왔을 경우에 break로 끊어서 바로 cnt를 출력하게
        if check():
            break
    if check():
        break
print(cnt)
    
