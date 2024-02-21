# import sys
# sys.stdin = open('input_s1.txt', 'r')

arr = [1,3,5,7,9]
N = len(arr)
def f(lst, n):
    cnt = 0
    K = int(input())
    for i in range(1<<n): # 2**N을 비트 연산자로 표기함.
        _sum = 0
        print(i, end= '==>')
        for j in range(n): # 0,1,2,3,4
            if i & (1 << j): # 000 & 000, 000 & 010, 000 & 100
                _sum += lst[j]
                print(lst[j], end=' ')
        if _sum == K:
            cnt += 1
        print()
        print(f'{cnt}', end= '\n')

f(arr, N) # [1,3,5,7,9], N = 5