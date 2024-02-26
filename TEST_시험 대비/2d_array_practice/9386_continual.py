



T = int(input())

for tc in range(1, T+1):

    N = int(input())
    string = input()
    cnt = 0
    max_cnt = 0
    for i in range(N):
        if string[i] == '1':
            cnt += 1
        elif string[i-1] == '1' and string[i] == '0':
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0
    if max_cnt < cnt:
        max_cnt = cnt
    print(f'#{tc} {max_cnt}')