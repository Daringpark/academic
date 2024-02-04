N = int(input()) # 처음 수 받기

maxV = 0 # 최대 출력값
for number in range(1, N):
    lst = [N, number]
    cnt = 2
    i=1
    check = 0
    while check >= 0:
        X = lst[i-1] - lst[i]
        lst.append(X)
        check = lst[i] - X
        i += 1
        cnt += 1

    if maxV < cnt:
        maxV = cnt
        ans = lst

print(maxV)
for x in ans:
    print(x, end=' ')