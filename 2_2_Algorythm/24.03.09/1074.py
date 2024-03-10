
N, r, c = map(int, input().split())
def Z(N, r, c):
    # 끝 2*2행렬에 도착했을 때
    if r == 0 and c == 0:
        return 0
    elif r == 0 and c == 1:
        return 1
    elif r == 1 and c == 0:
        return 2
    elif r == 1 and c == 1:
        return 3
    # 큰 행렬에 놓여 있을때,
    else:
        T = 2**(N-1)
        A = T**2 # 2**2(N-1)
        if r <= T-1 and c <= T-1: # 큰 영역을 기준 0,0에 있음
            return Z(N-1, r, c)
        elif r <= T-1 and  c > T-1: # 0, 1
            return A + Z(N-1, r, c-T) # T만큼 빼줘야 그 위치에 새로운 c를 통해서 하나 작은 영역의 새 영역을 확인 가능
        elif r > T-1 and c <= T-1:
            return 2*A + Z(N-1, r-T, c)
        elif r > T-1 and c > T-1:
            return 3*A + Z(N-1, r-T, c-T)
print(Z(N, r, c))