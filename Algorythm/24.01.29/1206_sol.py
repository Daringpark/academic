
# 승필 풀이
for tc in range(1, 11):   # tc 10개로 지정
    n = int(input())   # 건물 개수
    b_h = list(map(int, input().split()))   # 건물 높이 배열
    light_num = 0   # 채광 되는 변수 개수 
    for i in range(n):
        if b_h[i] > b_h[i-1] and b_h[i] > b_h[i-2] and b_h[i] > b_h[i+1] and b_h[i] > b_h[i+2]:   # 건물 높이 배열 기준 i번째 인덱스값이 양쪽 2개의 값보다 무조건 커야 함
            light_num += min(b_h[i] - b_h[i-1], b_h[i] - b_h[i-2], b_h[i] - b_h[i+1], b_h[i] - b_h[i+2])   # 높다는 전제 하에 양옆 2개 건물과의 차이 중 최소값을 채광 되는 변수에 더함
        else:   # 나머지의 경우는 넘어감
            continue
    print(f'#{tc} {light_num}')


# 여준이형 풀이
for num in range(10):
    cnt = int(input())
    b_lst = list(map(int, input().split()))
    sum = 0
    for i in range(2, len(b_lst)-2): # 값의 차이로만 비교해서 풀이함
        arr = []
        arr.append(b_lst[i] - b_lst[i-1])
        arr.append(b_lst[i] - b_lst[i-2])
        arr.append(b_lst[i] - b_lst[i+1])
        arr.append(b_lst[i] - b_lst[i+2])
        if min(arr) > 0: # 그 값이 양수가 될 때, 값을 추가하는 식
            sum += min(arr)
    print(f'#{num+1} {sum}')

# 지연이 풀이
for t in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for n in range(2, N-2):
        num_lst = [ lst[n]-lst[n-2], lst[n]-lst[n-1], lst[n]-lst[n+1], lst[n]-lst[n+2] ]
        x = min(num_lst)
        if x > 0:
            cnt += x
    print(f'#{t} {cnt}')