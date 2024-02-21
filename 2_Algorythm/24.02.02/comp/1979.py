import sys
sys.stdin = open('1979.txt', 'r')

T = int(input())
def my_count(key, lst):
    cnt = 0
    for i in range(len(lst)):
        if key == lst[i]:
            cnt += 1
    return cnt

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]

    length = [] # 연속되는 1의 길이를 담은 list
    for i in range(N): # 행 순회 길이 탐색
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
                if cnt > 0 and j == N-1:
                    length.append(cnt)
            else :
                if cnt > 0:
                    length.append(cnt)
                    cnt = 0

    for i in range(N): # 열 순회 길이 탐색
        cnt = 0
        for j in range(N):
            if matrix[j][i] == 1:
                cnt += 1
                if cnt > 0 and j == N-1:
                    length.append(cnt)
            else :
                if cnt > 0:
                    length.append(cnt)
                cnt = 0
    print(f'#{tc} {my_count(K, length)}')
