
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

# 구미 강사님 풀이
#1. 키보드부터 만지지 않는다.
#   단순하게 입력부터 받는거는 OK
# 머리속 또는 메모, 또는 그림 등등으로 문제를
# 어떻게 풀어 나갈지 아이디어를 완성
# 2. 아이디어를 순차적으로 나열
# 3. 나열된 아이디어를 코드로 옮기기
# view
# 조망권이라는거는  현재 건물 양옆 2칸내에 있는 건물 중
# 제일 높은 건물에 의해서 결정된다.
# 내 건물 높이 - 제일 높은 건물 => 조망권이 확보된 세대 수
# 내 건물 높이보다 높은건물이 있으면?? => 조망권 없음
# 양쪽 건물 네 개 살펴보고 제일 높은 건물이 나보다 낮으면 조망권 있음
# 1. 각 건물의 조망권 계산하기(반복문 돌기)
#    1-1 현재 건물 양쪽 두 칸에 있는 건물높이중 최고 층 찾기
#    1-2 조망권 세대 계산
# 2. 출력

# 조망권을 가지는 세대수 반환
def solve(data):
    sum_v = 0   #0은 더하기 연산에 영향을 끼치지 않음..
    # 각 건물 순회
    # 웬만하면...리스트 순회할 때 인덱싱으로
    for i in range(2,N-2): #양쪽 두 칸은 건물이 없음
        # i번째 건물의 조망권 계산을 위해서
        # i-2, i-1, i+1, i+2번째 건물들의 높이가 필요
        # 최대값 또는 최소값을 찾을 때, 초기값은 비교대상 내에서 가져가야 합니다.
        max_v = data[i-2]
        for b in [data[i-1],data[i+1],data[i+2]]:
            if max_v < b:
                max_v = b

        # 최대값 찾음! >>> 조망권 계산( 현재 건물(data[i] 과 비교)
        if data[i] > max_v:
            sum_v += data[i] - max_v

        # max_v = data[i-2]
        # for j in range(i-1,i+3):
        #     if j == i : # 조망권을 계산하려는 건물은 비교하면 안됨
        #         continue
        #     if data[j] > max_v:
        #         max_v = data[j]
        # if data[i] > max_v:
        #     sum_v += data[i] - max_v

    return sum_v

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int,input().split()))
    result = solve(data)
    print(f'#{tc} {result}')