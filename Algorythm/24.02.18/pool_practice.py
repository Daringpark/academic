
import sys
sys.stdout = open('output.txt', 'w')
import math

def find_ball():
    pass


def find_path():
    global pos
    global Hole
    cmt = 1e5
    for i in range(6):
        distance = round(math.sqrt((abs(Ball[0]-Hole[i][0])**2) + (abs(Ball[1]-Hole[i][1])**2)))
        if distance <= cmt:
            cmt = distance
            target_Hole = Hole[i]
    return target_Hole

def get_angle():
    if pos[0] <= Ball[0]:
        degree = math.acos((D**2+A**2-B**2)/(2*A*D))
        degree = round(math.degrees(degree))
        degree += 90
    else:
        degree = math.acos((D**2+A**2-B**2)/(2*A*D))
        degree = round(math.degrees(degree))
    
    if pos[1] > Ball[1]:
        degree = -(degree)
    else:
        pass
    return degree

pos = [50,50] # 내 공 위치
matrix = [[0] * 262 for _ in range(129)]
Hole = [[-3,-3], [-3,125], [-3,258], [130, -3], [130, 125], [130, 258]]
Ball = [117, 32]

A = (abs(Ball[0]-pos[0]))
B = (abs(Ball[1]-pos[1]))
D = round(math.sqrt(A**2+B**2))
matrix[pos[0]][pos[1]] = 'A' # 내 공
matrix[Ball[0]][Ball[1]] = 'T'

print(matrix)

for i in range(6):
    matrix[Hole[i][0]][Hole[i][1]] = 'X'



print(find_path())
print(get_angle())





