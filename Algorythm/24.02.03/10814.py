import sys
sys.stdin = open('10814.txt', 'r')
import sys
input = sys.stdin.readline

N = int(input())
user_data = {}
for _ in range(N):
    key, value = input().split() # map object를 만들기 필요가 없습니다.
    key = int(key)
    # if key in user_data:
    #     user_data[key].append(value)
    # else :
    #     user_data[key] = [value]
    user_data.setdefault(key, [])
    user_data[key].append(value)

for age in range(1, 201):
    if age in user_data:
        for name in user_data[age]:
            print(age, name)

    # N = len(user_data[age])
    # for i in range(N):
    #     print(age, user_data[age][i])