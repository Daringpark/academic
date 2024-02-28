

arr = ['A', 'B', 'C']
n = len(arr)

def get_sub_set(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end = '')
        tar >>= 1

for tar in range(1 << n):
    print('{', end = '')
    get_sub_set(tar)
    print('}')
print('==' * 10)


arr = ['a', 'b', 'c', 'd', 'e']
n = len(arr)

def get_sub(tar):
    res = ''
    for i in range(n):
        if tar & 0x1: # 타겟의 1비트가 1인지 확인하는 코드
            res += str(arr[i])
        tar >>= 1
    if len(res) >= 2:
        return f'{res}'

for tar in range(1 << n): #
    if get_sub(tar):
        print('{', end = '')
        print(get_sub(tar), end = '')
        print('}')
