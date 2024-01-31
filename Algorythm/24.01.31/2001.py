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
    space = []
    dead_count = []
    for i in range(N): # space에 파리 배치
        space.append(list(map(int, input().split())))

    # 파리채 만들어서 파리채 영역에서 sum하기 (my_sum사용, dead_count)
    for i in range(N-M+1):
        dead1 = []
        for j in range(i, i+M): # M*M matrix의 sum을 구하기 위해서
            for k in range(i, i+M):
                dead1.append(space[j][k]) # matrix에서 원소를 list 추가
        dead_count.append(my_sum(dead1))

    # 그 중에서 많이 잡은 개수를 출력 (my_max)
    most_dead = my_max(dead_count)

    print(f'#{tc} {most_dead}')