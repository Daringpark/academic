
A = int(input()) # -100부터 100이하
B = int(input()) # 목표 온도 A보다 큰 1 이상 100이하
C = int(input()) # 해동 이전 1도 올리기 위한 시간
D = int(input()) # 해동하는데 걸리는 시간 (0를 기준으로 얼어있고 안 얼어있고를 알 수 잇음)
E = int(input()) # 얼어있지 않은 고기를 1도 데우는데 걸리는 시간

if A < 0:
    print(abs(A)*C+D+(B*E))
else : print((B-A)*E)
