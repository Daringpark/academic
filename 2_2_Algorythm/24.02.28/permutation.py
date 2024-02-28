
def my_print():
    for j in range(K):
        print(arr[path[j]], end=' ')
    print(f'    ')

# permutation 만들기 (강사님)
def perm(lvl, N, K):
    if lvl == K: # 3에 도달했을 경우, (0,1,2)
        for j in range(K):
            print(arr[path[j]], end = ' ')
        print()

    for i in range(N):
        if not visited[i] and lvl < K: # lvl이 K와 같아졌을 때, path[lvl]을 돌지 않게 만들어주자.
            path[lvl] = i # level에 맞춰서 값을 집어넣어줌
            visited[i] = 1
            perm(lvl+1, N, K) # 재귀로 풀어낸다.
            visited[i] = 0

def combi(lvl, start):
    if lvl == K:
        my_print()
        return

    for i in range(start, N):
        if lvl < K:
            path[lvl] = i
            combi(lvl+1, start)

def combi2(lvl, start): # 중복 없는 조합 뽑기
    global cnt
    if lvl == K:
        my_print()
        cnt += 1
        print(cnt)
        return

    for i in range(start, N):
        if lvl <= K:
            path[lvl] = i
            combi(lvl+1, i+1) # range내에서 받아 오는 것이기 때문에 start 갱신은 i로 해줘야한다.

arr = [1,2,3,4,5,6]
N, K = 6, 2
path = [0] * K
visited = [0] * N
combi(0, 0) # 6*6 = 중복이 가능한 dice 조합
print("==" * 10)
arr = [1,2,3,4,5,6]
N, K = 6, 2
path = [0] * K
cnt = 0
combi2(0, 0) # 6C2 = 15 = 중복이 없는 조합
print("==" * 10)
perm(0, N, K) # 6*5 = 중복이 없는 dice 순열
