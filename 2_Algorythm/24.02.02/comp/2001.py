import sys
sys.stdin = open('2001.txt', 'r')

def my_sum(lst):
    sum_value = 0
    for number in lst:
        sum_value += number
    return sum_value
def my_max(lst):
    max_value = lst[0]
    for number in lst:
        if number > max_value:
            max_value = number
    return max_value

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    dead_count = []
    space = [list(map(int, input().split())) for _ in range(N)]
    # space에 파리 배치

    for nx in range(N-M+1): # 움직일 수 있는 바이너리 row
        for ny in range(N-M+1): # 움직일 수 있는 바이너리 col
            block = []
            for i in range(nx, nx+M): # 행 순회 방식으로 탐색 ->
                for j in range(ny, ny+M):
                    block.append(space[i][j])
            dead_count.append(my_sum(block)) # 파리채질마다 잡는 파리 수 저장

    most_dead = my_max(dead_count) # 새로운 리스트에서의 최대 파리 수 저장

    print(f'#{tc} {most_dead}') # 테스트 케이스마다 최대 파리수를 출력