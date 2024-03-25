def binary(k):
    res = ''
    for _ in range(4):
        if k%2: # 나머지가 1이 나온 경우, 뒤로 찍고 나가는 경우로 만들어야한다.
            res = '1' + res
        else:
            res = '0' + res
        k //= 2
    return res
# 7 = 0111
def de_binary(k):
    res = 0
    for i in range(3, -1, -1): # 뒤에서 부터 탐색하자
        if int(k[i]): #
            res += 2**(3-i)
    # 10이상 15이하 10 11 12 13 14 15
    if res >= 10:
        res %= 10
        res = alpha[res]   
    return str(res)

alpha = ['A', 'B', 'C', 'D', 'E', 'F']

T = int(input())
for tc in range(1, T+1):

    N, numbers = input().split()
    N = int(N)
    result = ''
    if N > 6: # 24비트의 경우
        for i in range(6):
            n = numbers[4*i:4*i+4]
            result += de_binary(n)
    else: # 16진수의 경우
        for number in numbers:
            n = int(number, 16)
            result += binary(n)
    print(f'#{tc} {result}')