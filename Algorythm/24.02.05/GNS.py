import sys
sys.stdin = open('gns.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    order, N = map(str, input().split())
    N = int(N)
    number_dict = {}
    number_a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(10):
        number_dict.setdefault(number_a[i], 0)

    lst = list(map(str, input().split()))
    for i in range(N): # O(N)
        number_dict[lst[i]] += 1

    res = ''
    for number in number_dict.keys():
        for _ in range(number_dict[number]):
            res = f'{res} {number}'
    res = res.strip()

    print(f'{order}\n{res}')