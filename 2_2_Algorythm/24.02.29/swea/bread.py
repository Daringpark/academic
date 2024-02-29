
import sys
sys.stdin = open("bread.txt")

### 1000 중 989
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     customers = list(map(int, input().split()))
#     COUNTS = [0] * (max(customers)//M+1)
#     for i in range(M, max(customers)+1):
#         if not COUNTS[i//M]:
#             COUNTS[i//M] = K
#     for customer in customers: # 직접 순회하면서 빼기
#         COUNTS[customer//M] -= 1
#         if -1 in COUNTS:
#             print(f'#{tc} Impossible')
#             break
#     else: print(f'#{tc} Possible')

### 812
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     customers = list(map(int, input().split()))
#     COUNTS = [0] * (max(customers)//M+1) # 0 ~ max//M
#     customers.sort()
#     for i in range(M, max(customers)+1):
#         if not COUNTS[i//M]:
#             COUNTS[i//M] = COUNTS[i//M-1] + K
#     for customer in customers: # 직접 순회하면서 빼기
#         if customer//M and customer%M:
#             for i in range(1, customer//M+1):
#                 COUNTS[i] -= 1
#             if -1 in COUNTS:
#                 print(f'#{tc} Impossible')
#                 break
#         else:
#             COUNTS[customer//M] -= 1
#             if -1 in COUNTS:
#                 print(f'#{tc} Impossible')
#                 break
#     else: print(f'#{tc} Possible')

'''
4 3 2
30 30 30 30
# Possible
'''

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    COUNTS = [0] * (max(customers)//M+1) # 0 ~ max//M # 33//3 = 0~11 (N = 12)
    customers.sort() # sorting을 해서 빨리 온 순서대로 처리할 수 있도록
    
    for i in range(M, max(customers)+1): # 붕어방 배열 저장
        if not COUNTS[i//M]:
            COUNTS[i//M] = COUNTS[i//M-1] + K # 그 당시에 얼마만큼 있을지
            
    for customer in customers: # 직접 순회하면서 빼기 # 진짜 초
        count_sec = customer//M
        for i in range(count_sec, len(COUNTS)):
            COUNTS[i] -= 1
        if -1 in COUNTS:
            print(f'#{tc} Impossible')
            break
    else : print(f'#{tc} Possible')
