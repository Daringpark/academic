import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    space = [input().strip() for _ in range(N)]
    res = ''
    #완전 탐색
    #행 순회
    for i in range(N):
        for j in range(N-M+1):
            if space[i][j:j+M] == list(reversed(space[i][j:j+M])):
                res = space[i][j:j+M]
                print(0)
                break
    
    #열 순회
    for i in range(N): # 열 순회
        for j in range(N-M+1): # 시작 위치에서 시작
            col = []
            for k in range(M): # col M의 길이 만큼 받아오기
                col.append(space[j+k][i])
            if col == col[::-1]:
                res = col
                print(1)

    print(f'#{tc} {"".join(res)}')