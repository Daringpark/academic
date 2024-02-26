# import sys
# sys.stdin = open('algo1_sample_in.txt', 'r')
# 테스트 케이스 확인용
#################################################

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]
    
    # 근처 4개의 풍선에서 점수 얻어오기
    dr = [-1,0,1,0] # 시계방향
    dc = [0,1,0,-1]
    flag = 0 # 시작은 12시부터
    
    res = 0 # 최대값을 바꾸기 위해서 미리 설정
    for row in range(1, N-1): # 가장자리 칸을 맞혀 상하좌우 중 일부 칸이 없는 경우는 세나 마나
        for col in range(1, N-1):
            A = 0
            B = space[row][col]
            for i in range(4):
                new_row = row + dr[i]
                new_col = col + dc[i]
                A += space[new_row][new_col] # 시계 방향에서 점수를 더해줌
            cnt = A - B # 매 회 결과가 되는 값
            if cnt > 0 and cnt%2 == 0:
                cnt = cnt * 2
            elif cnt > 0:
                pass
            else :
                cnt = 0

            if res < cnt : # 매 풍선마다 최고값을 갱신하는가
                res = cnt

    print(f'#{tc} {res}')