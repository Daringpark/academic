# number = [10,20,30,40]
# N = len(number)
# check = [0]*N
# def subset(k): # 0부터 시작하여 부분집합을 다 확인한다.
#     if k == N:
#         print(f'## {check} ##')
#         for i in range(N):
#             if check[i]:
#                 print(number[i], end = ' ')
#         print()
#     else :
#         for i in range(2):
#             check[k] = i
#             subset(k+1)
# subset(0)
# number = [10,20,30,40]
# N = len(number)
# check = [0]*N
# def subset(k, s, t): # 모든 부분집합의 합이 target 값을 도달할 때, 그 부분집합을 출력
#     if s == t: # 우리의 목표에 도달했을 경우
#         print(f'## {check} ##')
#         for i in range(N):
#             if check[i]:
#                 s += number[i]
#                 print(number[i], end = ' ')
#         print()
#     elif s > t: # 목표를 초과했을 경우
#         return
#     elif k == N: # depth 끝에 도달했지만, 목표를 얻지 못한 경우
#         return
#     else : # depth를 내려간다.
#         check[k] = 1
#         subset(k+1, s+number[k], t)
#         check[k] = 0
#         subset(k+1, s, t)
# subset(0, 0, 40)

N, M = 3,4
space = [[0]*M for _ in range(N)]
check = [0]*N # row에서 col값을 넣어줄 check_list
cnt = 0
def subset(k): #k는 row 탐색할 예정
    global space
    global cnt
    if k == N: # depth에 도달
        print(space)
    else:
        
        subset(k+1)


subset(0)