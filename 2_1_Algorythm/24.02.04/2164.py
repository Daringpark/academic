import sys
from collections import deque # deque library를 활용해서 시간복잡도를 줄여라.
input = sys.stdin.readline

N = int(input())

card = deque(range(1, N+1))
while len(card) != 1 :
    card.popleft()
    card.append(card.popleft())

print(card[0])