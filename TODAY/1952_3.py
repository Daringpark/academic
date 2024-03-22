
import sys
sys.stdin = open("1952.txt")
sys.stdout = open("1952_output_2.txt", "w")

T = int(input())
for tc in range(1, T+1):
    
    price = list(map(int, input().split()))
    months = list(map(int, input().split()))
    # 3000 * 30 * 12
    # 백준의 '퇴사'랑 유사한 방식
    # backward로 풀이하면 굉장히 쉽게 풀 수 있겠다. (이전 달의 일일권을 끊은 경우 + 이전 달의 한 달권 + 이전 달의 세 달권 끊은 경우)
    DP = [0] * 13 # DP table 0~11 + 12
    for i in range(11, -1, -1):
        DP[i] = min(DP[i+1]+months[i]*price[0], DP[i+1]+price[1])
        if i < 10:
            DP[i] = min(DP[i], DP[i+3]+price[2])

    min_value = min(DP[0], price[3])
    
    # print(DP)
    print(f'#{tc} {min_value}')