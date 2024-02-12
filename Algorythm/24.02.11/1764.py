import sys
input = sys.stdin.readline

M, N = map(int, input().split())
def make_set(number):
    K = set()
    for i in range(number):
        K.add(input())
    return K
A_set = make_set(M) # 듣도
B_set = make_set(N) # 보도
plus_set = list(A_set.intersection(B_set))
plus_set.sort() # 사전순 정렬
N = len(plus_set)
res = str(N)+'\n'+''.join(plus_set)
print(res)