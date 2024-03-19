def make_perfect(n, per):
    global max_per
    
    if n == N: # 끝까지 도달했다면
        # 기존의 0이랑 0.13 * 0.7 * 1.00
        
        # 기존의 최대값과 지금의 확률을 비교해서 큰 값을 취한다.
        max_per = max(max_per, per)
        return 
    
    # N은 최대 16개까지 이뤄짐
    # 재귀를 돌 때, 조건문으로 확인해야된다.
    for i in range(N):
        if not visited[i]: # 중복 체크 visited는 반복문의 idx를 따라야한다
            # 곱이 이뤄지는 순간 순간 체크해서 재귀를 돌지 말지 결정한다. > 그러면 아예 못 돌아
            if per*(matrix[n][i]/100) > max_per:
                visited[i] = 1
                make_perfect(n+1, per*(matrix[n][i]/100))
                visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # permutation + backtracking
    # N개의 일에 관련한 직원마다 성공률을 준다?
    visited = [0] * N
    max_per = 0
    make_perfect(0, 1)
    #format
    x = "{:.6f}".format(round(max_per*100, 6))
    print(f'#{tc} {x}')

'''
1
3
13 0 50
12 70 90
25 60 100
'''