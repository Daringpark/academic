
'''
배고픈 소 배시는 매일 저녁마다 헛간에 먹이가 있으면, 먹이를 하나 먹는다.
농부 존은 배시가 배 곪는걸 원하지 않는다.
그래서 먹이를 주문해서 그 날 아침에 배송온다.
di는 10**14까지, 하루 주문량 bi 10**9까지

N, T가 입력으로 주어지는데
다음 N줄은 di와 bi가 주어진다.
처음 T일 동안 얼마나 많은 양을 먹었는지 출력하라

2 5
1 2
5 10 이렇게 입력이 이뤄지면

5일이 되었을 때, 얼마나 많은 양의 먹이를 먹을까?
첫날 아침에 먹이가 2개가 배달 되고,
이건 2일차까지 먹을 수 있다.
5일 아침이 되어서 10개의 먹이가 왔지만,
5일 저녁에 1개 먹고 나서
총 5일 저녁까지 먹은 양은 3개다.

2 5
1 10
5 10이면
1일차에 10개의 식량을 받았기 때문에
5일 저녁까지는 넉넉히 먹을 수 있다.

di 는 무조건 커지는 식으로 증가하고,
bi 는 그냥 주어진다. (1이상으로)
'''
# T일에 1개 이상의 먹이가 주어지느냐 아니냐에 따라서 +1을 해주냐 아니냐가 차이가 난다.
# T-1 까지의 먹이 합을 구한다음에 이 양이 T-1보다 크다면, 그냥 T-1을 하는거고
# 그게 아니라면, sum한 값만큼 뽑으면 될 듯



import sys
input = sys.stdin.readline

N, T = map(int, input().split())
hale = 0
# O(N) 10**5
days = []
counts = []
for _ in range(N):
    d, b = map(int, input().split())
    days.append(d)
    counts.append(counts)
days.append(T+1)
days.append(0)

result = 0
for i in range(N):
    hale += counts[i]
    if days[i+1] - days[i] < hale: # 그 날짜까지 버틸 수 있는가를 확인
        # 충분하다
        hale -= days[i+1] - days[i]
        result += days[i+1] - days[i]
    else : # 굶을 날이 생긴다.
        result += hale
        hale = 0

print(result)