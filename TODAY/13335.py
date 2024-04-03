# 13335 트럭

import sys
from collections import deque


# 

# N은 다리를 건너는 트럭 개수, W는 다리의 길이, L은 다리의 하중을 나타낸다.
N, W, L = map(int, input().split())
Trucks = deque(map(int, input().split())) # 한 트럭의 무게는 10을 넘지 않는다.



Bridge = [0] * W
Completed = []
turn = 0

# 다리의 길이가 존재한다.
# 


# while len(Completed) != N:
#     while len(Bridge) <= W or sum(Bridge) <= L:
#         if Trucks:
#             item = Trucks.popleft()
#         else: pass

#         if len(Bridge) <= W and sum(Bridge)+item <= L:
#             Bridge.append(item)
#             turn += 1
#             print(turn, Trucks, Bridge, item)
#         elif Bridge and Trucks:
#             Trucks.insert(0, item)
#             break
#         else:
#             # Trucks.insert(0, item)
#             break

#     while Bridge: # Bridge 비우기
#         Completed[-1] = (Bridge.pop(0))
#         zeroornot = Completed.pop(0)
#         if zeroornot:
#             Completed
#         turn += 1
# print(turn)


















