
# 참외밭

counting_list = [0]*4 # 1,2,3,4
x = []
y = []


'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''

N = int(input()) # 1 제곱평방미터에서 자라는 참외의 개수
counting_dict= {}
for i in range(4):
    counting_dict.setdefault(i, [])
for i in range(6): # 6번의 입력을 받을 예정
# 1,2는 동, 서 (가로 방향); 3,4는 남, 북 (세로 방향)
    direction, amount = map(int, input().split())


