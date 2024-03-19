# 예제 코드 // Permutation
arr = [1,2,3,4]
N = len(arr)
K = 2
path = [0] * K # 0이 arr 원소로 없어야 한다.
####################
# 위는 입력으로 받는다고 가정한다.

def choice(n):
    if n == K: # 재귀 leveling permutation
        print(*path)
        return
    
    for i in range(len(arr)): # arr의 길이만큼을 그래야 가능
        if arr[i] in path: # 값 자체를 받아야함
            continue
        path[n] = arr[i]
        choice(n+1) # 재귀를 들어갔다가 빠져나오고 나서
        path[n] = 0 # 원복해주는 과정이 무조건 필요함

choice(0)