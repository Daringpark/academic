import sys
sys.stdin = open('10804.txt')

T = int(input())
# 무식하게 그냥 if-elif 4개
for tc in range(1, T+1):
    raw_data = input()
    N = len(raw_data)
    res = ''
    for i in range(N):
        if raw_data[i] == 'b':
            res = res + 'd'
        elif raw_data[i] == 'd':
            res = res + 'b'
        elif raw_data[i] == 'p':
            res = res + 'q'
        else:
            res = res + 'p'
    res = res[::-1]
    print(f'#{tc} {res}')