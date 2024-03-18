def search():
    x = y = 0 # 탐색을 시작할 위치
    pos_x = pos_y = 1 # 최대값을 품은 좌표를 저장; 우선 임의값으로 배정
    sum_value = 0 # 매 시행마다 초기화되지 않음
    if M == 1:  # while 내부에서 계속 조건문을 돌 필요 없음; 해당 값만 뽑으면 된다.
        return matrix[x][y]
    while x != pos_x or y != pos_y: # M >= 2:
        if pos_x == 1 and pos_y == 1:
            pass
        else : x, y = pos_x, pos_y
        max_value = 0 # 순회마다 초기화됨
        for row in range(M):
            for col in range(M): # M*M 순회
                new_row = x + row
                new_col = y + col
                if 0 <= new_row < N and 0 <= new_col < N: # 범위 안만 파악
                    if max_value < matrix[new_row][new_col]:
                        max_value = matrix[new_row][new_col]
                        pos_x = new_row
                        pos_y = new_col
        if (x, y) != (pos_x, pos_y):
            sum_value += max_value
    return  sum_value

T = int(input()) # 테스트케이스의 개수가 주어지고
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N >= M
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # matrix 불러오기
    print(f'#{tc} {search()}')