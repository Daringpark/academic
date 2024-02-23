'''
[1,2,3] 라는 배열이 주어질 때, 이것들의 부분 집합을 구하자.
'''

# N = 3
# result = [-1] * N
#
# def construct_candidates(c):
#     # node 한개를 기준으로 3개의 다발로 뻗어 나갈때, 뻗어나가는 것이 1씩 커질 때
#     c[0] = 0
#     c[1] = 1
#     return 2
#
# def recur_g(depth):
#     if depth == N: # 3 2 1 0
#         print(result)
#         # for i in range(N):
#             # if result[i]:
#                 # print(result[i])
#         # print()
#         return
#     c = [0]*100
#     nC = construct_candidates(c)
#     for i in range(nC): # 최종 depth까지
#         result[depth] = i
#         recur_g(depth+1) # bottom-up 방식 # 0, 1, 2
# recur_g(0)

N = 5
ex_set = [1,2,3,4,6]
result = [0]*N
def subset(depth): # 현재 depth로부터 부분집합 구하기

    if depth == N:
        # print(result) # 부분집합 보기
        sumV = 0 # 각 부분집합의 합을 시행마다 초기화
        for i in range(N):
            if result[i]:
                sumV += ex_set[i]
        if sumV == 10:
            print(result, end = ' ')
            for i in range(N):
                if result[i]:
                    print(ex_set[i], end = ' ')
            print()
    else:
        for i in range(2):
            result[depth] = i
            subset(depth+1)

subset(0)