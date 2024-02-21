import sys
sys.stdin = open('1945.txt')

T = int(input())

for tc in range(1, T+1):
    count_list = [0]*5 # a,b,c,d,e
    numbers = [2,3,5,7,11]
    N = int(input())

    for num in numbers:
        while N % num == 0:
            count_list[numbers.index(num)] += 1
            N //= num

    res = ' '.join(map(str, count_list))

    print(f'#{tc} {res}')