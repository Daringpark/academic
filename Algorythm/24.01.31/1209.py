import sys
sys.stdin = open('1209.txt', 'r')
# 정방 행렬의 대각합 구하기 개념
# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
#
# sumV = 0
# res = 0
# for i in range(N):
#     sumV += lst[i][i] + lst[i][N-1-i] # 한 줄로 우하향, 우상향 대각선 더하기
# res = sumV - lst[N//2][N//2] # 홀수개수 정사각형일때, 중복 제거
# print(res)
def my_max(lst):
    max_value = lst[0]
    for number in lst:
        if number > max_value:
            max_value = number
    return max_value
T = 10
for tc in range(1, T+1):
    N = int(input())
    M = 100
    matrix = [list(map(int, input().split())) for _ in range(M)]
    value_list = []
    value_c1 = 0
    value_c2 = 0
    for i in range(M):
        value_x = 0
        value_y = 0
        for j in range(M):
            value_x += matrix[i][j]
            value_y += matrix[j][i] # 정방 행렬이니 이렇게 가능
        value_c1 += matrix[i][i]
        value_c2 += matrix[i][M - 1 - i]

        if value_x not in value_list :
            value_list.append(value_x)  # row 고정
        if value_y not in value_list :
            value_list.append(value_y)  # row 고정
    value_list.extend([value_c1, value_c2])

    print(f'{N} {my_max(value_list)}')