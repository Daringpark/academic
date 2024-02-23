


print(bin(20)) # 10진수를 2진수로 표현
print(hex(20)) # 10진수를 16진수로 표현
print(int(10)) # default 진수는 10진수
print(int('a', 16)) # 16진수로 표현된 값을 10진수로 변환
print(int('1010', 2)) # 2진수로 표현된 integer를 10진수로 변환


# Bit Comparasion
print('27 OR 20', 27 | 20)


# 도전 문제
print(0b11011110 & 0b11011)
print(0b11011)
print(0x4A3 | 25)
print(0x4A3)

# XOR ENCODING DECODING
print(7070^1004)
print(1004^6258)
# 도전 문제 Encoding
def encoding_decoding(x):
    return x^1004
print(encoding_decoding(1000))
print(encoding_decoding(4))

# LEFT, RIGHT SHIFT OPERATOR
print(1<<2) # 100
print(1<<4) # 10000
print(3<<3) # 3000 # 0cta
# 도전 : 반복문을 사용하여 2진수와 10진수로 출력하시오. 0b1, 0b10, 0b100, 0b1000, 0b10000
for i in range(5):
    x = 1<<i
    print(f'{bin(x)} {x}')

# Condition with bits
x = '1111'
N = len(x)
x = int(x, 2)
res = ''
for n in range(N):
    if x & (1<<n):
        res += '1'
    else :
        res += '0'
print(res)

# MSB 0 = +, 1 = -
# x = '47FE'
# N = len(x)
# res = ''
# for i in range(N):
#     print(x[i])
#     per_letter = int(x[i], 16)
#     res += bin(per_letter)[2:]
# print(res)

# 10726
N, M = 6, 15

M = bin(M)[2:]
print(type(M))
cnt = 0
for i in range(N):
   x = str(M)
   n = len(x)
   if n-1-i >= 0 and x[n-1-i] == '1':
       cnt += 1
if cnt == N:
    print("ON")
else: print("OFF")

# 도전 컴퓨터가 연산한 실수 값을 출력해보자.
x = 0.1
print(f'{x:.25f}')