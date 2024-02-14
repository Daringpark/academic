def f(i, k, t):
    global cnt
    if i == k:
        ss = 0
        for j in range(k):
            if bit[j]:
                ss += A[j]
        if ss == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ')
            cnt += 1
            print()
    else: # Back-tracking point
        for j in range(1, -1, -1): # Bit-masking
            bit[i] = j
            f(i+1, k, t)
# This is not even Back-tracking Algorythm

N = 8
A = [1,2,3,4,7,8,9,10]
bit = [0]*N
cnt = 0
f(0, N, 9)