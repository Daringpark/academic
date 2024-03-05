

# R, C <= 500 // 배열을 새로 만들기에는 25000개의 데이터가 쓰일 수 있음
# 2차원 리스트를 2개 만든다? >> 시간 초과 날 것??
# DP는 결국 메모이제이션 문제인 것 같다.
# 어느 위치로 가야할지 정한 것을 재귀한다.


r, c = map(int, input().split())
Matrix = [list(map(int, input().split())) for _ in range(r)]
new_Matrix = [[0] * c for _ in range(r)]
direction_list = [[0] * c for _ in range(r)]
drdc = [[0,0], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

for row in range(r):
    for col in range(c):
        numbers = []
        for direction in drdc: # 일단 값을 보고, 유효한 값인지 확인 + 위치 저장
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < r and 0 <= new_col < c:
                numbers.append([Matrix[new_row][new_col], [new_row, new_col]]) # 값과 위치
        # 다 돌고 나오면, numbers에서 값을 기준으로 한 최소값 쪽으로 공을 던진다.
        A = min(numbers, key=lambda x: x[0])[1] # 그 타일에서 넘
        x, y = A[0], A[1]
        # 이동 구현을 여기에서 해야되겠네
        move_row = row
        move_col = col
        cnt = 1
        while [move_row, move_col] != A:
            move_row, move_col = A[0], A[1]
            if [move_row, move_col] == [row, col]:
                cnt += 1
            direction_list[row][col] = [move_row, move_col]
        new_Matrix[move_row][move_col] += cnt

        print(direction_list)
        print(new_Matrix)

for i in range(r):
    print(*new_Matrix[i])

# for i in range(r):
#     print(*Matrix[i])

'''
1 6
10 20 3 4 5 6
'''


'''
4 4
20 2 13 1
4 11 10 35
3 12 9 7
30 40 50 5
'''