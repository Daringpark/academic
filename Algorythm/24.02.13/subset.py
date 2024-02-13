def f(i, k):
    if i == k :
        for j in range(k):
            if bit[j]:
                print(arr[j], end = ' ')
            print()
    else:
        for j in range(2):
            bit[i] = j
            f(i+1 , k)

N = 4
arr = [1,2,3,0]
bit = [0]*N
f(0, N)