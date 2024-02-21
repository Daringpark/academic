import sys
sys.stdin = open('4837.txt', 'r')
# 부분집합 구하기

T = int(input())
A = list(range(1,13))

for tc in range(1, T+1):
    N, K = map(int, input().split()) # N은 원소의 개수, K는 원소의 합
    cnt = 0 # 개수 세기
    for i in range(1<<12): # 2**N을 비트 연산자로 표기함.
        _sum = 0 # K와 비교를 위해서
        new_set_list = []
        # 0123456789...
        for j in range(12): # 0,1,2,3,4
            if i & (1 << j): # 000 & 000, 000 & 010, 000 & 100
                _sum += A[j]
                new_set_list.append(A[j])
        if _sum == K and len(new_set_list) == N: # 한 번의 시행에서 K값과 원소의 합이 같을 때
            cnt += 1

    print(f'#{tc} {cnt}')