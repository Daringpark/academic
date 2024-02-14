import sys
sys.stdin = open('cardgame.txt')

def function(s,e):
    if s == e : # if s < e: << 이걸로 돌렸을 때, 그 끝 값을 받아오는 알고리즘이 아님
        return s  # if start_point == end_point: # 값을 받아낸다.
        # 재귀 돌리기
    medium = (s + e) // 2  # 분할 정복의 파티션 설정
    winner1 = function(s, medium)
    winner2 = function(medium + 1, e)
    return winner(winner1, winner2)  # 가위바위보에서 승리한 카드 (가위, 바위, 보 중 하나)

def winner(a, b): # 123 가위바위보
    X, Y = space[a-1], space[b-1]
    # a 승리 조건
    if (X == 2 and Y == 1) or (X == 3 and Y == 2) or (X == 1 and Y == 3):
        return a
    # b 승리 조건
    elif (X == 1 and Y == 2) or (X == 2 and Y == 3) or (X == 3 and Y == 1):
        return b
    else: return a

T = int(input())
for tc in range(1, T+1):
    start = 1
    end = int(input())
    space = list(map(int, input().split())) #[1,3,2,1]
    print(f'#{tc} {function(start, end)}')