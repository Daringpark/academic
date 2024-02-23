import sys
sys.stdin = open("password.txt")

def x0tonumber(number):
    if not number.isdigit(): # 16진수 to 10진수
        P = ord(number) - 55
    else:
        P = int(number)
    point = ''
    for i in range(4): # 10진수 to 2진수 변환
        point = str(P%2) + point
        P //= 2
    return point # 2진수 string으로 들어가게 된다.
def make_matrix():
    for i in range(N): # row
        res = ''
        for j in range(M): # col
            res += x0tonumber(matrix[i][0][j])
        new_matrix[i].append(res)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # row, col
    matrix = [input().split() for _ in range(N)]
    new_matrix = [[] for _ in range(N)]
    make_matrix()

    # new_matrix에서 7개의 고유번호를 찾아야한다.
    # 각 숫자는 0과 1 비율이 존재한다. 7개로 떨어지는게 아니라 7의 배수로 떨어지게 된다.


    res = 0
    print(f'#{tc} {res}')