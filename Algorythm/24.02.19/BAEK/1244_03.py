
N = int(input()) # 전구의 개수는 100개 이하
light_list = list(map(int, input().split())) # 1,0으로 표현된 N개의 전구
Action_N = int(input()) # 액션 갯수
def light_switch(order):
    global light_list
    if light_list[order] == 1:
        light_list[order] = 0
    else:
        light_list[order] = 1
def result():
    for i in range(N):
        print(light_list[i], end = ' ')
        if N > 20 and (i+1)%20 == 0:
            print()
for i in range(Action_N):
    sex, number = map(int, input().split())
    amount = number//20
    rest = number%20
    # 남성은 number의 배수이면, 스위치를 바꿔준다.
    # 여성은 지정한 지점부터 끝 범위까지(오른쪽이 더 가까우면 오른쪽을 기준으로 N) 변경해주어야함.
    if sex == 1: # 남성일 경우
        if number == 1: # 전체 바꿔주기
            for i in range(N):
                light_switch(i)
        else:
            for i in range(1, N+1): # N = 27까지 있고, 3의 배수라면
                if i%number == 0: # 3은 나머지가 0이면서
                    light_switch(i-1) # 리스트 내에서 2번째 것을 전환해주어야 함.
    else: # 여성일 경우
        light_switch(number-1)
        if N-number >= number: # 오른쪽이 더 멀 때, 왼끝까지 가보자
        # 오른쪽 끝에서 넘버까지의 수가 더 가까운지, 왼쪽 끝에서 넘버까지의 수가 더 가까운지
        # 거리의 차이를 통해서 판별하고자 한다.
        # 범위 설정이 중요하다.
            for i in range(number):
                if light_list[number-1-i] == light_list[number-1+i]:
                    pass
                else:
                    i -= 1
                    break
            for j in range(1, i+1):
                light_switch(number - 1 - j)
                light_switch(number - 1 + j)
        else: # 오른쪽이 더 가까울 때, 오른끝까지 가보자
            for i in range(N-number+1): # 얼마만큼 스위치를 조절할건지 탐색
                if light_list[number-1-i] == light_list[number-1+i]:
                    pass
                else:
                    i -= 1
                    break
            for j in range(1, i + 1): # 실제 스위치 변환
                light_switch(number - 1 - j)
                light_switch(number - 1 + j)
result()
