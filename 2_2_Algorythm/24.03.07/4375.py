
import sys
input = sys.stdin.readline

### 문자열 활용
# while True: 
#     try:
#         N = int(input())
#         idx = 1
#         X = 1
#         while X%N != 0:
#             idx += 1
#             X = int('1'*idx)
#         print(idx)
#     except:
#         break

### 수학 활용
while True:
    try:
        N = int(input())
        T = 1%N
        idx = 1
        while T != 0:
            idx += 1
            T = (T*10+1)%N # 11 111 1111 한 칸씩 올리려면 1%N부터 시작해서 10*T+1
        print(idx)
    except:
        break