import sys
sys.stdin = open('input_s1.txt', 'r')

bit = list(map(int, input().split()))

def changeable():
    for i in range(2):
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                for l in range(2):
                    bit[3] = l
                    for m in range(2):
                        bit[4] = m
# 비트 연산자의 이해 1<<N == 2**N

N = 4
for i in range(1<<N): # 0부터 16(N-1)이 되기 전 수까지
    print(i)
# 비트 마스킹
print(7&5) #111 & 101 # 비트 마스킹의 1을 비교해서 1인 경우만 뽑는다.
print(53&45) #110101 & 101101 # 총 4개를 비교하게 됨. # 100101 = 1 + 4 + 32