N = int(input())

cnt = 0
for _ in range(N):
    blank = []
    word = list(input())

    for i in range(len(word)):
        blank.append(word.pop())

        if len(blank) >= 2 and blank[-1] == blank[-2]:
            blank.pop()
            blank.pop()
    if blank == []:
        cnt += 1

print(cnt)