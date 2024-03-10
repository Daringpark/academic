T = int(input())
for tc in range(T):
    N, text = input().split()
    N = int(N)
    res = ''
    for letter in text:
        res += letter * N
    print(res)