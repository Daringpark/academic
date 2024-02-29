
import sys
sys.stdin = open("backroom.txt")

# 어제 그리디 문제스러운데?
# 돌아가야할 방향이 다른 학생과 크거나 같으면 cnt += 1
# 10 중 2
## 그리디라고 생각했는데 추가적인 중복이 생기게 된다.
# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input()) # 학생수
#     students= [] # 현재와 돌아가야할 배열을 저장한다.
#     for _ in range(N):
#         students.append(list(map(int, input().split())))
#     students.sort(key = lambda x: x[1])
#     cnt = 1
#     end = students[0][1]
#     for idx in range(1, N):
#         if end >= students[idx][0]:
#             cnt += 1
#             end = students[idx][1]
#     print(f'#{tc} {cnt}')
'''
10 30
50 60
20 77 
27 62
84 35
1 + 3
'''


### 10 중 7
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # 학생수
#     students= [] # 현재와 돌아가야할 배열을 저장한다.
#     arr = [0] * 201 # 0(0,1) ~ 199(398,399), 200(400)
#     for _ in range(N):
#         start, end = map(int, input().split())
#         start //= 2
#         end //= 2
#         if start < end :
#             for i in range(start, end + 1):
#                 arr[i] += 1
#         else:
#             for i in range(end, start + 1):
#                 arr[i] += 1
#     print(f'#{tc} {max(arr)}')
#  1 2 3 4가 나왔을 경우 겹치지 않는데 바로 위 코드는 겹친다.


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 학생수
    students= [] # 현재와 돌아가야할 배열을 저장한다.
    arr = [0] * 201 # 0(1) ~ 199(398,399), 200(400)
    max_value = 0
    for _ in range(N):
        start, end = map(int, input().split())
        if start%2:
            start = start//2 + 1
        else: start //= 2
        if end%2:
            end = end//2 + 1
        else: end //= 2
        # 홀수번일때, 1과 2를 겹치게 하고 싶다면, 한 idx에 저장하는게 맞다.
        if start < end :
            for i in range(start, end + 1):
                arr[i] += 1
        else:
            for i in range(end, start + 1):
                arr[i] += 1

    print(f'#{tc} {max(arr)}')







