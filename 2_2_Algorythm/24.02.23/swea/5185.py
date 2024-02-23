
# 무식하게 그냥 추가하기
T = int(input())
for tc in range(1, T+1):
    res = ''
    N, letter = input().split()
    N = int(N)
    for i in range(N):
        x = bin(int(letter[i], 16))[2:]
        n = len(x)
        if n != 4:
            res += (4-n)*'0'+x
        else: res += x
    print(f'#{tc} {res}')
    
# 딕셔너리 활용 - 성은님
T = int(input())
dict0x = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
for tc in range(T):
    N, num0x = input().split()
    str2 = ''
    for idx in range(int(N)):
        str2 += dict0x[num0x[idx]]
    print(f'#{tc + 1} {str2}')

# int, binary 변환 없이
def hexTodec(s): # 16진수 변환하기
    result = 0
    for c in s:
        if c.isdecimal():
            result += int(c)
        else: # A = ord 65
            result += ord(c) - 55
    return result
def decTobin(num):
    s = ''
    for _ in range(4): # 나머지를 추가해준다.
        s = str(num % 2) + s
        num //= 2
    return s

T = int(input())
for tc in range(1, T + 1):
    N, hexS = input().split()
    result = []
    for c in hexS:
        result.append(decTobin(hexTodec(c)))
    print(f'#{tc}', end=' ')
    print(*result, sep='')