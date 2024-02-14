def f(i, k, s, t): # summation을 매 node마다 유망성을 본다.
    global cnt
    if s == t: # 타겟이랑 같을 때,
        for j in range(k):
            if bit[j]:
                s += A[j]
                print(A[j], end = ' ')
        cnt += 1
        print()
        print(f'### {cnt}')
    elif i == k :
        return
    elif s > t :
        return
    else: # Back-tracking point
        # for j in range(1, -1, -1): # Bit-masking
        #     bit[i] = j
        #     f(i+1, k, s+A[i], t)
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)
N = 8
A = [1,2,3,4,7,8,9,10]
bit = [0]*N
cnt = 0
f(0, N, 0, 9)