import socket
import time
import math


def angle_cal(x, y):
    ax = abs(x)
    ay = abs(y)

    rad = math.atan2(ax, ay) if y != 0 else 0

    if ax == 0:
        if ay > 0:
            return 0
        else:
            return 180
    elif ay == 0:
        if ax > 0:
            return 90
        else:
            return 270
    elif x > 0 and y > 0:
        return math.degrees(rad)

    elif x < 0 and y > 0:
        return 360 - math.degrees(rad)

    elif x < 0 and y < 0:
        ang = math.degrees(rad) + 180
        return ang
    elif x > 0 and y < 0:
        ang = 180 - math.degrees(rad)
        return ang
    else:
        return 0


def distance_cal(x, y):
    dis = math.sqrt((x**2+y**2))
    return dis


# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU01_SEONGJUN'

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
HOLES = [[2, 2], [125, 2], [252, 2], [2, 125], [125, 125], [252, 125]]

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

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]


    # 오더의 번호마다 타겟을 변경
    if order == 1:
        target_lst = [1, 3, 5]
    else:
        target_lst = [2, 4, 5]

    print(target_lst)

    # 타겟의 x좌표, y좌표 초기화
    tBall_x = 0
    tBall_y = 0

    # 적은 번호의 목적구부터 타겟으로 설정하고 만약 홀에 들어가면 다음 목적구
    for i in target_lst:
        if balls[i][0] != -1 and balls[i][1] != -1:
            tBall_x = balls[i][0]
            tBall_y = balls[i][1]
            print(tBall_x, tBall_y)
            break

    # 타겟과 흰공의 벡터
    xV = tBall_x - whiteBall_x
    yV = tBall_y - whiteBall_y
    t_degree = angle_cal(xV, yV)

    # 구멍과 타겟의 벡터 리스트 생성
    hall_xV = [(HOLES[i][0] - tBall_x) for i in range(6)]
    hall_yV = [(HOLES[i][1] - tBall_y) for i in range(6)]

    # 구멍과 벡터리스트를 돌며 가장 가까운 구멍 확인
    near_lst = []
    for i in range(6):
        hx = hall_xV[i]
        hy = hall_yV[i]
        h_degree = angle_cal(hx, hy)
        near_lst.append(abs(h_degree - t_degree))
    print(near_lst)

    # 가장 가까운 구멍의 인덱스 확인
    min_idx = 0
    minV = 360
    for i in range(6):
        if near_lst[i] < minV:
            minV = near_lst[i]
            min_idx = i

    # 가장 일직선상에 가까운 구멍 벡터와 목적구 벡터
    HXV = hall_xV[min_idx]
    HYV = hall_yV[min_idx]
    H_dis = distance_cal(HXV, HYV)
    print(HXV, HYV)

    # 흰공을 이동시킬 좌표
    mx = 5.73 * math.cos(math.atan2(HYV, HXV))
    my = 5.73 * math.sin(math.atan2(HYV, HXV))
    print(mx, my)
    mov_X = tBall_x - mx
    mov_Y = tBall_y - my

    # 흰공으로 움직여야될 거리
    dx = mov_X - whiteBall_x
    dy = mov_Y - whiteBall_y

    print(t_degree)

    angle = angle_cal(dx, dy)
    distance = distance_cal(dx, dy)
    if distance < 10:
        power = 20
    else:
        power = distance * 0.8


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