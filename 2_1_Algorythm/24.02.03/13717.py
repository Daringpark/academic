import sys
sys.stdin = open('13717.txt', 'r')

N = int(input())
pokemon = []
cnt_list = []
for i in range(N):
    pokemon.append(input())
    K, M = map(int, input().split())

    cnt = 0
    while M//K != 0:
        M = M - K
        cnt += 1
        M += 2
    cnt_list.append(cnt)

print(sum(cnt_list))
print(pokemon[cnt_list.index(max(cnt_list))])