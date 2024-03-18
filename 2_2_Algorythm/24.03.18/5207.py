
# 서치를 할때 좌우 판별이 필요하다
def Binary_search(num, lt, rt, f): # 값과 A 리스트의 0 ~ N-1 인덱스값과 비교한다.
    if lt > rt: # 끝까지 돌았을 때
        return

    # f로 판별을 하자.
    # 만약 0 1, 1 1(왼) > 1 2 (오) 은 오케이
    # 0 1(오), 1 1(왼) > 2 1 (왼) 은 안 오케이
    mid = (lt + rt)//2
    if num == A[mid]: # 값이 아예 뜬 경우,
        return 1
    elif num > A[mid]: # 중간값 초과인 경우 오른쪽을 취한다.
        if f != 1: # 0 혹은 2가 왔을 경우,
        # if check == 'left' or check == '':
            f = 1
            return Binary_search(num, mid+1, rt, f)
    elif num < A[mid]: # 중간값 미만인 경우 왼쪽을 취한다.
        if f != 2:
            f = 2
            return Binary_search(num, lt, mid-1, f)
    return 0


T = int(input())
for tc in range(1, T+1):
    
    N, M = map(int, input().split()) # A 리스트 개수와 B 리스트 개수
    # A는 정렬이 되어 있고, B에 있는 원소들을 A에 넣어서 들어있는지 없는지 확인한다.
    # 앞의 조건을 만족하면서, 번갈아서 선택할 수 있는 경우 (좌우좌우, 우좌우좌와 같은 경우)
    # 복잡도는 log N
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    A.sort()
    for number in B:
    # 1 <= N <= 500,000
        flag = 0
        # check = ''
        if Binary_search(number, 0, N-1, flag): # 조건을 만족했을 때,
            cnt += 1
    print(f'#{tc} {cnt}')
    

'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
6 3
1 3 5 7 9 11
2 4 6
'''

'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''

'''
1
10 4
1 2 3 4 5 6 7 8 9 10
10 6 5 1
'''