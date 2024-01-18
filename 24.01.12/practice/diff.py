
a = list(map(int, input().split()))
#n = len(a)
maxV = 0
minV = 10000
sumV = 0
cnt = 0

#mean
for i in a :
    cnt += 1    

# mean_result = sum(a)/n

for i in range(cnt) :
    sumV = sumV + a[i]
mean_result = sumV/cnt

for i in range(cnt) :
    if maxV < a[i]:
        maxV = a[i]

for i in range(cnt):
    if minV >= a[i]:
        minV = a[i]
validation = maxV - minV

print(mean_result, validation)

