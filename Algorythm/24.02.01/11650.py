import sys
input = sys.stdin.readline

N = int(input())

dot_list = []
for trial in range(N):
    dot_list.append(list(map(int, input().split())))
dot_list = sorted(dot_list)
for dot in dot_list:
    print(dot[0], dot[1])

# for i in range(N-1):
#     min_idx = i
#     for j in range(i+1, N):
#         if dot_list[min_idx][0] > dot_list[j][0]: # 우선적으로, X 좌표를 맞추기
#             min_idx = j
#             # if dot_list[i][0] == dot_list[i+1][0] and dot_list[i][1] > dot_list[i+1][1]:
#             #     dot_list[i], dot_list[i+1] = dot_list[i+1], dot_list[i]
#     dot_list[min_idx], dot_list[i] = dot_list[i], dot_list[min_idx]
#     min_idx = i
#     for j in range(i+1, N):
#         if dot_list[min_idx][1] > dot_list[j][1]: # 우선적으로, X 좌표를 맞추기
#             min_idx = j
#     dot_list[min_idx], dot_list[i] = dot_list[i], dot_list[min_idx]
# for i in range(N):
#     print(dot_list[i][0], dot_list[i][1])


### 백준 11650 좌표 정렬하기 sort(key = )
# N = int(input())

# points = []
# for trial in range(N):
#     points.append(list(map(int, input().split())))
# points.sort(key = lambda x:(x[0], x[1]))

# for point in points:
#     print(point[0], point[1])







