import sys
sys.stdin = open("1952.txt")
sys.stdout = open("1952_output_1.txt", "w")

T = int(input())
for tc in range(1, T+1):
    
    price = list(map(int, input().split()))
    months = list(map(int, input().split()))
    # 3000 * 30 * 12
    # 백준의 '퇴사'랑 유사한 방식 : forward
    months = [0] + months
    DP = [0] * 13 # DP table 0~11 + 12
    for i in range(1,13):
        # 11월, 12월은 3달권을 고려할 수 없을 것 idx 10, 11, 12
        # 처음 그 전달의 누적과 일일권, 한달권을 비교한다.
        DP[i] = min(DP[i-1]+price[0]*months[i], DP[i-1]+price[1])
    
        # 그 다음에 세달권짜리랑 비교했을 때, 더 값싼가?
        if i >= 3:
            DP[i] = min(DP[i], DP[i-3]+price[2])
    min_value = min(DP[-1], price[3])
    
    # print(DP)
    print(f'#{tc} {min_value}')