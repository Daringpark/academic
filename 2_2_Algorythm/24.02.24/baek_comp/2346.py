'''
5
3 2 1 -3 -1
'''
from collections import deque
N = int(input())
Balloons = deque(enumerate(map(int, input().split())))
poped = deque()
while Balloons:
    idx, amount = Balloons.popleft() # 값을 받아온다.
    poped.append(idx+1)
    if amount > 0: # 양수의 경우
        Balloons.rotate(-(amount-1)) # idx의 양만큼 오른쪽으로 이동
    elif amount < 0: # 음수의 경우
        Balloons.rotate(-amount) # 오른쪽으로 양수 방향
print(' '.join(map(str, poped)))