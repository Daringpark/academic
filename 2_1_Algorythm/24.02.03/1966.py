import sys
sys.stdin = open('1966.txt', 'r')


## 68ms
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    pos = M
    x = lst[M]
    cnt = 1
    while max(lst) != x or pos != 0: #내가 원하는 숫자가 최대값이면서 제일 앞에 올 때,
        if max(lst) != lst[0]: # 리스트 안의 최대값이 오기 전까지
            if pos == 0: # 만약 pos = 0 일때, 포지션부터 변경해준다.
                pos = len(lst) # 새로운 리스트의 길이를 받아야 한다.
            q = lst.pop(0) # Queue에서 빼고 넣어준다.
            lst.append(q)
            pos -= 1 # N-1로 자동으로 배치됨. (내가 원하는 수의 위치가)
        if lst[0] == max(lst): # 제일 앞의 수가 최대값일 때, Queue에서 빼줌.
            lst.pop(0) # 값을 없애줌
            if pos == 0:
                break
            cnt += 1 # 번째를 높혀줌
            pos -= 1 # 포지션은 땡겨줌
    print(cnt)