t = int(input())

for test_case in range (1, t+1) :
    n = int(input())
    numbers = list(map(int, input().split()))
    max_count = 0
    x = 0
    for k in numbers :
        cnt = numbers.count(k)
        if max_count < cnt : 
            max_count = cnt
            x = k
    print("#"+str(n), str(x))