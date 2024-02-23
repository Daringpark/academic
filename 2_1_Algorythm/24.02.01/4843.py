import sys
sys.stdin = open('4843.txt', 'r')

# T = int(input())
#
# # brute force
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     for i in range(N-1): # 전체 오름차순 정렬 #bubble_sort
#         for j in range(i+1, N):
#             if numbers[i] > numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#
#     for i in range(N-1): # bubble_sort
#         for j in range(i+1, N):
#             if i%2 == 0  and numbers[i] < numbers[j]: # 홀수번째 0 2 4는 내림차순
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#     numbers = numbers[:10]
#     res = ' '.join(map(str, numbers))
#     print(f'#{tc} {res}')
# # for문을 4개 돌리는 경우라 시간 복잡도가 증가

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
if i % 2 == 1:
    minIdx = i
    for j in range(i + 1, N):
        if numbers[j] < numbers[minIdx]:
            minIdx = j

    numbers[i], numbers[minIdx] = numbers[minIdx], numbers[i]

else:
    maxIdx = i
    for j in range(i + 1, N):
        if numbers[j] > numbers[maxIdx]:
            maxIdx = j
#
#     numbers[i], numbers[maxIdx] = numbers[maxIdx], numbers[i]

#     list_length = 10 #길이를 조절 할 수 있음
#     for i in range(list_length):
#         if i%2 == 1: #짝수번째 일반 선택 정렬을 해야됨
#             minidx = i
#             for j in (i+1, N):
#                 # if numbers[minidx] > numbers[j]:
#                 if numbers[j] < numbers[minidx]:
#                     minidx = j
#             numbers[i], numbers[minidx] = numbers[minidx], numbers[i]
#         else :
#             maxidx = i
#             for j in range(i+1, N):
#                 if numbers[j] > numbers[maxidx]:
#                     maxidx = j
#             numbers[i], numbers[maxidx] = numbers[maxidx], numbers[i]
#
#     print(f'#{tc}', *numbers[:10])


    print(f"#{t + 1}", *numbers[:10])

