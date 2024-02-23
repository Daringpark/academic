N, m, M, T, R = map(int, input().split())

# N분 운동하는 것이 목표, 운동을 하거나 휴식하거나 둘 중 하나로 결정
# m은 최소 맥박, M은 최대 맥박
# 운동을 하는경우 X+T, 휴식을 하는경우 X-R
pulse = m # 초기 맥박은 m
cnt = 0 # 실시간 운동 측정
turn = 0 # 실시간 시간 측정
while cnt != N:
    if T > M - m:
        break
    if m <= pulse+T <= M: # 운동을 하는 경우
        pulse += T
        N -= 1
        turn += 1
    else: # 운동을 하지 않는 경우
        turn += 1
        pulse -= R
    if pulse < m: # 맥박이 최소 미만으로 내려 갔을 경우 
        pulse = m
if cnt == N : print(turn)
else : print(-1)