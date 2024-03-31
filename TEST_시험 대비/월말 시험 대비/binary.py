


def make_binary(number):
    res = ''
    for _ in range(4):
        if number%2:
            res = '1' + res
        else:
            res = '0' + res
        number //= 2
    return res

T = int(input())
for tc in range(1, T+1):

    N, numbers = input().split()
    result = ''
    for n in numbers:
        N = int(n, 16)
        result += make_binary(N)
    print(f'#{tc} {result}')