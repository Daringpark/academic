T = int(input())

for tc in range(1, T+1):
    word = input()
    #Pythonic code with slicing
    if word == word[::-1]:
        res = 1
    else:
        res = 0
    print(f'#{tc} {res}')