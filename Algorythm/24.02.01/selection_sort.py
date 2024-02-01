
A = [4,2,63,25,73,14,68,35,55,23]
n = len(A)

def Asort(lst, N):
    cnt = 0

    for i in range(N-1):
        for j in range(i+1, N):
            if lst[i] > lst[j]:
                cnt += 1
                lst[i], lst[j] = lst[j], lst[i]
    return cnt, lst
print(Asort(A, n)) #(N*(N-1))//2 = 45

A = [4,2,63,25,73,14,68,35,55,23]
n = len(A)

def selection_sort(lst, N):
    cnt = 0
    for i in range(N-1):
        minidx = i # 마지막 인덱스의 전까지 비교할 예정
        for j in range(i+1, N): # i 다음 수와 비교할 예정
            if lst[minidx] > lst[j]:
                minidx = j
        cnt += 1
        lst[i], lst[minidx] = lst[minidx], lst[i] # 제일 앞으로 보내니까
    return cnt, lst
print(selection_sort(A, n)) # N-1 = 9

A = [4,2,63,25,73,14,68,35,55,23]
n = len(A)
def Bubble_Sort(lst, N) :
    cnt = 0
    for i in range(N-1, 0, -1) : # 끝에서부터 1까지 -1 단위로
        for j in range(0, i) : # 0부터 N-2 까지의 j
            if lst[j] > lst[j+1] : # j+1 = N-1까지 고정 가능
                cnt += 1
                lst[j], lst[j+1] = lst[j+1], lst[j] # A의 0번째에 숫자 고정
    return cnt, lst
print(Bubble_Sort(A, n))





### join 사용하지 않고, 불러서 출력
for tc in range(1, 4):
    N = 5
    A = []
    for i in range(N):
        A.append(i)
    A[tc] += 100

    print(f'#{tc}', end = ' ')
    for j in range(N):
        print(A[j], end= ' ')
    print()