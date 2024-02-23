import sys
sys.stdin = open('input_1208.txt', 'r')

def my_max(lst): # max func
    max_value = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    return max_value

def my_min(lst): # min func
    min_value = lst[0]
    for i in range(len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
    return min_value

for i in range(1, 11): # 테스트 케이스는 10개 주어진다.
    N = int(input()) # 덤프횟수 <= 1000
    space = list(map(int, input().split())) # 각 높이를 int 리스트로 받는다.

    for idx in range(N):
        max_in_space = my_max(space)
        min_in_space = my_min(space) # min, max 받아서 비교하기
        space[space.index(max_in_space)] -= 1
        space[space.index(min_in_space)] += 1 # min max 블럭 덤핑
    max_in_space = my_max(space)
    min_in_space = my_min(space) # 그 회차 덤핑 이후, max - min 을 비교해서 출력
    ans = max_in_space - min_in_space
    print(f'#{i} {ans}')

# def my_max(x):
#     maxV = x[0]
#     for i in range(len(x)):
#         if maxV < x[i]:
#             maxV = x[i]
#     return maxV
# def my_min(x):
#     minV = x[0]
#     for i in range(len(x)):
#         if minV > x[i]:
#             minV = x[i]
#     return minV
# for t in range(1, 11):
#     N = int(input())
#     boxes = list(map(int, input().split()))
#
#     for i in range(N):
#         maxV = my_max(boxes)
#         minV = my_min(boxes)
#         max_idx = boxes.index(maxV)
#         min_idx = boxes.index(minV)
#         boxes[max_idx] -= 1
#         boxes[min_idx] += 1
#
#     maxV = my_max(boxes)
#     minV = my_min(boxes)
#     ans = maxV - minV
#
#     print(f'#{t} {ans}')