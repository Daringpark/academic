# Combination code
def combination(level, start): # 3가지 뽑기
    
    if level == K: # 5C3 = 5 4 3 / 3 2 1 = 10
        print(*res)
        return
    
    for i in range(start, N-K+level+1):
        res[level] = arr[i] # level의 값
        combination(level+1, i+1)
    
# Combination code
def combination2(level, start): # 3가지 뽑기
    
    if level == K: # 5C3 = 5 4 3 / 3 2 1 = 10
        print(*res)
        return
    
    for i in range(start, N):
        res[level] = arr[i] # level의 값
        combination2(level+1, i+1)
    
arr = [1,2,3,4,5]
N = len(arr)
K = 3 # level
res = [-1] * K

arr = [1,2,3,4,5]
N = len(arr)
K = 3 # level
res = [-1] * K

combination(0, 0) # 초기 단이 level 0이니까
print()
combination2(0, 0) # 초기 단이 level 0이니까
