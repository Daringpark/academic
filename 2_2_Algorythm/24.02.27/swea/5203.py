import sys
sys.stdin = open("5203.txt")

def solve():
    player1 = []
    player1_counts = [0] * 10
    player2 = []
    player2_counts = [0] * 10
    for i in range(0, 12): # 0 1 / 2 3 / 4 5 / 6 7 / 8 9 / 10 11
        if i%2: # 2 플레이어에 주기
            player2.append(cards[i])
            player2_counts[cards[i]] += 1
        else: # 1 플레이어에 주기
            player1.append(cards[i])
            player1_counts[cards[i]] += 1
        if len(player1) >= 3: # (3,2), (3,3), (4,3) ...
            # TRIPLET 확인하기
            for j in range(10):
                if player1_counts[j] >= 3:
                    return 1
                elif player2_counts[j] >= 3:
                    return 2
            # RUN 확인하기
            for j in range(8): # 0 ~ 7; 7 8 9
                if player1_counts[j] >= 1 and player1_counts[j+1] >= 1 and player1_counts[j+2] >= 1:
                    return 1
                elif player2_counts[j] >= 1 and player2_counts[j+1] >= 1 and player2_counts[j+2] >= 1:
                    return 2
    return 0
T = int(input())
# 1,2 는 플레이어, 0이면 무승부
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    print(f'#{tc} {solve()}')
