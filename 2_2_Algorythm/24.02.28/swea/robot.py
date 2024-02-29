


T = int(input())
for tc in range(1, T+1):
    lst  = input().split()
    N = int(lst[0]) # N 회 실행할 명령
    pos = {'B' : 1, 'O' : 1} # dictionary로 로봇들의 position을 저장한다.
    # 첫 실행 로봇
    robot, x = lst[1], int(lst[2])

    pre_robot = robot # 이전과 다른 로봇일 경우, 이동할 수 있다.
    pos[pre_robot] = x # 이동을 시키고나서 버튼을 누른 것까지 생각
    pre_time = x # 다른 로봇이 이동을 할 수 있게 시간 비교용 변수
    total = pre_time

    for i in range(3, len(lst), 2):
        robot, x = lst[i], int(lst[i+1])
        if pre_robot == robot: # 같은 경우 똑같이 이동한다.
            time = abs(x-pos[robot])+1

            pre_time += time # pre_time은 유지 # 다른 로봇이 이동할 수 있는 시간을 벌어준다.
        else: # 다른 경우, 같이 이동하면 된다.
            # time = max(1, abs(x-pos[robot]) - pre_time + 1)
            # 한 줄로 코딩할 수 있다. max method를 활용하여 비교할 수 있음

            time = abs(x - pos[robot]) # 다른 로봇이 걸어가는 시간
            if time > pre_time: # 추가 이동을 해야되는가?
                time = time - pre_time + 1
            else: # 움직이고 그냥 기다리기
                time = 1
                
            pre_time = time # pre_time을 새로 갱신해줘야 함.
        total += time
        pre_robot = robot
        pos[pre_robot] = x





