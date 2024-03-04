





T = int(input())
for _ in range(1, T+1):

    coin = [25, 10, 5, 1]
    money = []
    # 쿼터 25, 다임 10, 니켈 5, 페니 1
    change = int(input()) # received change
    for c in coin:
        money.append(change//c)
        change -= change//c*c
    print(*money)