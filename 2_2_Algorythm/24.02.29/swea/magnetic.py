
import sys
sys.stdin = open("magnetic.txt")

# def col_check(col):
#     cnt = 0
#     is_red = False # flag
#     for row in range(N): # 0~99까지 순회
#
#         if Table[row][col] == 1: # 그 전 아무것도 없이 처음 N 자성체를 만날 경우
#             is_red = True
#         elif is_red and Table[row][col] == 2: # 이전에 N 자성체를 만났었고, S 자성체를 만날 경우
#             cnt += 1
#             is_red = False # 자성체 도막을 끊어서 카운트를 갱신해준다.
#     return cnt
# # for tc in range(1, 11):
# for tc in range(1, 11):
#
#     N = int(input()) # 100
#     Table = [list(map(int, input().split())) for _ in range(N)]
#     # N극이 1, S극이 2
#     # row 탐색을 먼저해서 col별 red를 밀어주는 걸 확인하자
#     sum_value = 0
#     for i in range(N):
#         sum_value += col_check(i)
#     print(f'#{tc} {sum_value}')


#### 이건 스택 자료구조를 이용하면 쉽게 풀 수 있다.
def col_stack_check(col): # col row
    cnt = 0
    table_stack = [] # 큐라고 생각해도 될 듯? 그냥 배열에다가 저장해서 쓴 거 ㅇㅇ..
    for row in range(N):
        if Table[row][col] == 1: # 먼저 N극이 나온 경우, 스택에 추가해준다.
            table_stack.append(Table[row][col])
        elif table_stack and Table[row][col] == 2 and table_stack[-1] != Table[row][col]: # S극이 나중에 나온 경우로 만들어준다.
            # 우선 스택은 차 있어야 되고, 스택의 끝이 N극이어야되며, 현재 나온 값은 S극이어야한다.
            table_stack.append(Table[row][col]) # S극을 똑같이 추가해줘야지 NNSS를 한개의 자석으로 본다. 안그러면 개수 ++
            cnt += 1
    return cnt

for tc in range(1, 11):
    N = int(input()) # 100
    Table = [list(map(int, input().split())) for _ in range(N)]
    sum_value = 0
    for i in range(N):
        sum_value += col_stack_check(i)
    print(f'#{tc} {sum_value}')



'''
#1 471
#2 446
#3 469
#4 481
#5 481
#6 501
#7 488
#8 476
#9 464
#10 490
'''

