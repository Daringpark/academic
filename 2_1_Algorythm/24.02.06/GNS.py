import sys
sys.stdin = open('gns_input.txt')

digits = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for tc in range(1,T+1):
    tmp = input()
    arr = list(map(str, input().split()))

    cnts = {}
    for item in arr:
        if cnts.get(item):
            cnts[item] += 1
        else:
            cnts[item] = 1
    
    result = ''.join(list(map(lambda n:(n+' ')*cnts[n], digits)))
    print(f'#{tc}\n{result}')