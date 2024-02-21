import sys
sys.stdin = open('11723.txt')

import sys # 59% 시간 초과
import copy

import sys
input = sys.stdin.readline
N = int(input())
S = set()
all_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

def solve():
    global S
    for _ in range(N):
        command = input().split()
        if len(command) == 2:
            amount = int(command[-1])
            if command[0] == 'add' and amount not in S:
                S.add(amount)
            elif command[0] == 'remove' and amount in S:
                S.remove(amount)
            elif command[0] == 'check':
                if amount not in S:
                    print(0)
                else:
                    print(1)
            elif command[0] == 'toggle':
                if amount not in S:
                    S.add(amount)
                else:
                    S.remove(amount)
        else:
            if command[0] == 'all':
                S = copy.deepcopy(all_set)
            else:
                S = set()
solve()

