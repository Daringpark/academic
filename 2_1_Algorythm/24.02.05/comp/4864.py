import sys
sys.stdin = open('input_4864.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input() # N개
    str2 = input()

    if str1 in str2:
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')
