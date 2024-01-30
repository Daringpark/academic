
N = 3
lst = [1,2,3,4,5]

## 완전 탐색의 경우, 5*5*5
cnt = 0
for i in lst:
    for j in lst:
        for k in lst:
            cnt += 1
            print(i,j,k)
print(cnt)

print("-"*20)

## 5P3 의 Greedy  5*4*3 = 60
cnt = 0
for i in lst :
    for j in lst :
        if j == i :
            continue
        for k in lst :
            if k == i or k == j :
                continue
            cnt += 1
            print(i, j, k)
print(cnt)