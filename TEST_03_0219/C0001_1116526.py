import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU01_PARKMINCHEOL'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    def find_hole(): # 앞에 있는 것을 고려하지 않고, 일단 홀 위치를 받아서 넣을 구멍을 선택함.
        global target_hole_pos
        global min_value_dis
        for hole in HOLES:
            A = abs(targetBall_x - hole[0])
            B = abs(targetBall_y - hole[1])
            target_hole_distance = math.sqrt(A**2+B**2)
            if target_hole_distance < min_value_dis:
                min_value_dis = round(target_hole_distance)
                target_hole_pos = [hole[0], hole[1]]

    def get_angle():
        global angle
        # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
        # 일직선으로 쳤을 때, 홀이 없으면 무용지물
        if whiteBall_x == targetBall_x:
            if whiteBall_y < targetBall_y: # 윗 방향이 0도
                angle = 0
            else:
                angle = 180 # 아래 방향이 180도
        elif whiteBall_y == targetBall_y:
            if whiteBall_x < targetBall_x: # 오른쪽에 있을 때, 90도
                angle = 90
            else:
                angle = 270 # 왼쪽에 있을 때, 270도

        # 1사분면에 있을때,
        if whiteBall_x < targetBall_x and whiteBall_y < targetBall_y: # atan(width/height)
            big_theta = math.atan(width/height) if height > 0 else 0 # radian으로 얻어짐
            r2_2 = round(4*(5.73**2)) # 공 반지름 2개의 제곱
            new_pos = [targetBall_x+round(math.sqrt(2)*5.5), targetBall_y-round(math.sqrt(2)*5.5)] # 아래 위치를 잘 잡아야되는데
            new_distance = math.sqrt((abs(whiteBall_x - new_pos[0]))**2+(abs(whiteBall_y - new_pos[1]))**2)
            Y = math.acos(((distance**2)+(new_distance**2)-r2_2)/(2*distance*new_distance))
            # angle = math.degrees(big_theta - Y)
            angle = math.degrees(math.atan(width/height))
            print(1, angle)

        # 2사분면에 있을때,
        elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
            big_theta = math.atan(height/width) if height > 0 else 0 # radian으로 얻어짐
            r2_2 = round(4*(5.73**2)) # 공 반지름 2개의 제곱
            # min_value_dis r2_2

            new_pos = [targetBall_x+round(math.sqrt(2)*5.5), targetBall_y+round(math.sqrt(2)*5)]
            new_distance = math.sqrt((abs(whiteBall_x - new_pos[0]))**2+(abs(whiteBall_y - new_pos[1]))**2)
            Y = math.acos(((distance**2)+(new_distance**2)-r2_2)/(2*distance*new_distance))
            angle = 270 + math.degrees(big_theta - Y)
            print(2, angle)

        # # 3사분면에 있을때,
        elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
            big_theta = math.atan(width/height) if height > 0 else 0 # radian으로 얻어짐
            r2_2 = round(4*(5.73**2)) # 공 반지름 2개의 제곱
            new_pos = [targetBall_x, targetBall_y+round(math.sqrt(2)*5.5)]
            new_distance = math.sqrt((abs(whiteBall_x - new_pos[0]))**2+(abs(whiteBall_y - new_pos[1]))**2)
            Y = math.acos(((distance**2)+(new_distance**2)-r2_2)/(2*distance*new_distance))
            angle = 180 + math.degrees(big_theta - Y)
            angle = math.degrees(big_theta - Y) + 180
            # angle = math.degrees(math.atan(width/height)) + 180
            
        #     print(3, angle)

        # # 4사분면에 있을때,
        elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
            big_theta = math.atan(height/width) if height > 0 else 0 # radian으로 얻어짐
            r2_2 = round(4*(5.73**2)) # 공 반지름 2개의 제곱
            new_pos = [targetBall_x, targetBall_y+round(math.sqrt(2)*5.5)]
            new_distance = math.sqrt((abs(whiteBall_x - new_pos[0]))**2+(abs(whiteBall_y - new_pos[1]))**2)
            Y = math.acos(((distance**2)+(new_distance**2)-r2_2)/(2*distance*new_distance))
            angle = 90 + math.degrees(big_theta - Y)
            angle = math.degrees(big_theta) + 
        #     print(4)




        #
        # # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
        # if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        #     radian = math.atan(width / height)
        #     angle = (180 / math.pi * radian) + 180
        #
        # # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
        # elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        #     radian = math.atan(height / width)
        #     angle = (180 / math.pi * radian) + 90

        return angle

    def next_ball():
        global targetBall_x
        global targetBall_y
        global number
        target = balls[number] # 1, 3, 5
        if target[0] == -1 and target[1] == -1:
            number += 2
            target = balls[number]
        if number == 6:
            number = 5
            target = balls[number]
        targetBall_x = target[0]
        targetBall_y = target[1]

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]
    if order == 1:
        number = 1
    else:
        number = 2
    next_ball()
    targetBall_x = balls[number][0]
    targetBall_y = balls[number][1]
    print(targetBall_x, targetBall_y)
    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    # radian = math.atan(width / height) if height > 0 else 0
    # angle = math.degrees(radian)

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width**2 + height**2)
    print(distance)

    target_hole_pos = []
    min_value_dis = 1e5
    find_hole()
    angle = get_angle()
    min_value_dis # small d
    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.6

    print(number)





    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')