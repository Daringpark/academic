import sys
sys.stdin = open('gns.txt', 'r')

# T = int(input())
# number_a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# for tc in range(1, T+1):
#     order, N = map(str, input().split())
#     N = int(N)
#     number_dict = {}
#     for i in range(10):
#         number_dict.setdefault(number_a[i], 0)
#
#     lst = list(map(str, input().split()))
#     for i in range(N): # O(N)
#         number_dict[lst[i]] += 1
#
#     res = ''
#     for number in number_dict.keys():
#         for _ in range(number_dict[number]):
#             res = f'{res} {number}'
#     res = res.strip()
#
#     print(f'{order}\n{res}')

####### counting sort
T = int(input())
number_a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    order, N = map(str, input().split())
    N = int(N)
    string = list(input().split())

    count_list = [0]*10
    ans = [0]*N # 개수 만큼의 str 숫자들을 저장

    for i in string:
        count_list[number_a.index(i)] += 1
    for i in range(1, 10): # 누적합
        count_list[i] = count_list[i-1] + count_list[i]

    for letter in string:
        idx = number_a.index(letter)
        ans[count_list[idx] - 1] = letter
        count_list[idx] -= 1
    print(f'#{tc} {" ".join(ans)}')