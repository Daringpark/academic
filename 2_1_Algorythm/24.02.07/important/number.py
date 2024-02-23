import sys
sys.stdin = open('number.txt')

### counting sort
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) # 길이가 50 이하
    counting_sort = [0] * (max(arr) + 1)  # 해당 숫자까지의 인덱싱을 만들어주고

    for num in arr:  # count_list에 ++
        counting_sort[num] += 1

    for i in range(1, len(counting_sort)):  # 누적 합으로 계산
        counting_sort[i] += counting_sort[i - 1]

    result_list = [0] * len(arr)  # arr의 길이 만큼
    for num in arr:
        i = counting_sort[num]
        result_list[i - 1] = num
        counting_sort[num] -= 1

    result_list = list(map(str, result_list))
    result = ' '.join(result_list)
    print(f'#{tc} {result}')