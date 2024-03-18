
def partition(start, end):
    pivot = end
    i = start - 1
    
    for j in range(start, end):
        if A[j] < A[pivot]:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    # 마지막에 pivot을 제 위치에 돌려두기
    A[i+1], A[pivot] = A[pivot], A[i+1]
    return i+1 # 이 위치가 피봇의 위치

def quick_sort(left, right):
    # 어떤 값 pivot을 설정해서
    # 그 수의 왼쪽과 오른쪽은 작고 큰수로 분류한다
    if left < right: # 같거나 left가 클 때, X
        # 파티션을 기준으로
        m  = partition(left, right)
        
        quick_sort(left, m-1)
        quick_sort(m+1, right)
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    # 0부터 N-1까지의 quick_sort
    quick_sort(0, N-1)
    # print(A)
    print(f'#{tc} {A[N//2]}')