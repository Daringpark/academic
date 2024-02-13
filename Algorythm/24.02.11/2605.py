
N = int(input())
card = list(map(int, input().split()))
order = []
for i in range(N):
    order.insert(i-card[i], str(i+1))
res = ' '.join(order)
print(res)