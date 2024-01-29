N = int(input())
lst = list(map(int, input().split()))

max_value = 0
for i in range(N-1) :
    cnt = 0
    for j in range(i+1, N-1) :
        if lst[i] > lst[j] :
            cnt += 1
    if max_value < cnt :
        max_value = cnt
print(max_value)