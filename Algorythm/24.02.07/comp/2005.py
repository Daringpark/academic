import sys
sys.stdin = open('2005.txt')

### memorization이 필요함!!!!!!!
## 파스칼 삼각형
# def pascal(n):
#     if N == 1:
#         res = [1]
#     elif N == 2:
#         res = [1, 1]
#     else:
#         res = [1] * n
#         for i in range(n):
#             if i == 0 or i == n-1:
#                 pass
#             else : res[i] = pascal(n-1)[i] + pascal(n-1)[i-1]
#     return res

## TEST CASE AND PRINT
# T = int(input())
#
# for tc in range(1, T+1):
#
#     N = int(input())
#     result = ''
#     for i in range(1, N+1):
#         result += f'\n'
#         result += " ".join(list(map(str, pascal(i))))
#
#     print(f'#{tc} {result}')

##### memorization을 이용한거 맞아???
def pascal(n):
    global memo
    if n == 1 :
        memo[n] = [1]
    elif n == 2:
        memo[n] = [1, 1]
    else:
        for i in range(1, n-1): # 0, n-1 끝 값을 range 밖에 두게하고
            memo[n][i] = memo[n-1][i] + memo[n-1][i-1] # 메모에 쌓아뒀던 데이터를 이용함???
        memo[n][0] = memo[n][n-1] = 1 #
    return memo[n]

## TEST CASE AND PRINT
T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N : 파스칼 삼각형의 길이
    memo = [[i]*i for i in range(N+1)] # memo의 이름으로 이차원 배열을 만들어줌

    # OUTPUT
    result = ''
    for i in range(1, N+1): # string화
        result += f'\n'
        result += " ".join(list(map(str, pascal(i))))

    print(f'#{tc} {result}')