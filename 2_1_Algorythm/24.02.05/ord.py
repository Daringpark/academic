# chr(31) == 0
# chr(41) == 'A'
# chr(61) == 'a'
# 아스키 코드 연습
a = ord('f') - ord('a') + ord('A') # ord('F')
print(chr(a))

def atoi(value):
    r = 0
    for c in value:
        r = r*10 + (ord(c) - ord('0'))
    return r

t = atoi('32')
print(t, type(t))

def iota(value):
    res = ''
    while value != 0:
        c = chr(ord('0') + value%10)
        res = c + res
        value = value//10
    return res

t = iota(32)
print(t, type(t))


K = 'Korean and American'
K_list = list(map(str, K))
K_list.reverse()
res = ''
for i in range(len(K_list)):
    res = res + K_list[i]
print(res)