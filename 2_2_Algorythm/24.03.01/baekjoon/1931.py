
import sys
sys.stdin = open("1931.txt")
input = sys.stdin.readline

import sys
input = sys.stdin.readline

N = int(input())
reserve_list = []
for _ in range(N):
    room_reserve = list(map(int, input().strip().split()))
    reserve_list.append(room_reserve)
reserve_list.sort(key = lambda x : (x[1], x[0]))
end = -1
cnt = 0
for i in range(N):
    if end <= reserve_list[i][0]:
        cnt += 1
        end = reserve_list[i][1]
print(cnt)