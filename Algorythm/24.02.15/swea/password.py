import sys
sys.stdin = open('password.txt')

def cycle(): # 한 싸이클
    for i in range(1, 6):
        item = password.pop(0)
        item -= i
        password.append(item)
        if password[-1] <= 0:
            password[-1] = 0
            break
for tc in range(1, 11):
    N = input()
    password = list(map(int, input().split()))

    while password[-1] != 0:
        cycle()

    print(f'#{N}', end = ' ')
    print(*password)



