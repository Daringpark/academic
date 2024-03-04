

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site_password = dict()
for _ in range(N):
    key, value = input().strip().split()
    site_password[key] = value

for _ in range(M):
    key = input().strip()
    print(site_password[key])