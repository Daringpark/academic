

# 50개 테케, 10초
def cook(n, lstA, lstB):
    global min_value
    if len(lstA) > N//2 or len(lstB) > N//2:
        return
    
    if n == N:

        if len(lstA) == len(lstB): # N//2로 쪼개질 때
            sum_A = sum_B = 0
            for i in range(N//2):
                for j in range(N//2):
                    sum_A += matrix[lstA[i]][lstA[j]]
                    sum_B += matrix[lstB[i]][lstB[j]]
            
            min_value = min(min_value, abs(sum_A-sum_B))
            return
    cook(n+1, lstA+[n], lstB)
    cook(n+1, lstA, lstB+[n])

T = int(input())
for tc in range(1, T+1):

    # 4이상 16이하 짝수
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_value = 1e7 # 원소 하나는 2만 이하
    TeamA = []
    TeamB = []
    cook(0, TeamA, TeamB)
    print(f'#{tc} {min_value}')

