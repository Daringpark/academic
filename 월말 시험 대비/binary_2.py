T = int(input())

for test_case in range(1, T + 1):
    N = float(input())
    binary = ''
    while N != 0:
        N *= 2
        if N >= 1:
            binary += '1'
            N -= 1
        else:
            binary += '0'
        if len(binary) > 12:
            binary = 'overflow'
            break
    print(f"#{test_case} {binary}")