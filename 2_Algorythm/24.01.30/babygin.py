# 0부터 9까지의 숫자 트럼프카드를 임의로 6장 뽑았을 때,
# 3장이 연속적인 번호를 갖는 경우를 Run
# 3장이 동일한 번호를 갖는 경우를 Triplet
# 6장의 카드가 Run and Triplet으로 이뤄진다면, Baby-gin이라고 한다.
# 6개의 숫자를 받아 baby-gin인지 파악할 수 있는가?

# N = int(input())

# Brute Force // 완전 탐색 기법 (모든 경우의 수를 확인하는 기법)
# Greedy // 탐욕 탐색 기법 (해당 상황에서 최적의 탐색 기법)

# 기본 구성
num = 456789

cnt_list = [0] * 12 # 트리플렛을 고려해서? # 10, 11까지

for i in range(6) :
    cnt_list[num%10] += 1 #9 8 7 6 5 4
    num //= 10 #나머지가 때어진 몫만 45678, 4567, 456, 45, 4 
# print(cnt_list)

## 완전 탐색 기법을 활용해야 한다.
## 트리플렛 확인 이후, 런을 확인하는 경우로 해야 탐색 속도를 줄일 수 있을 것이다.
## 런 확인 이후 트리플렛을 하는 경우, 탐색하고(값을 빼고) 처음부터 재탐색한다.

idx = 0 # 초기 확인 위치
tri = run = 0 # 초기 세팅

while idx < 10 : # idx가 10으로 가면 while문은 멈추게 된다.
    if cnt_list[idx] >= 3 :
        cnt_list[idx] -= 3
        tri += 1
        continue
    if cnt_list[idx] >= 1 and cnt_list[idx+1] >= 1 and cnt_list[idx+2] :
        cnt_list[idx] -= 1
        cnt_list[idx+1] -= 1
        cnt_list[idx+2] -= 1
        run += 1
        continue
    idx += 1

if run + tri == 2 : print('Baby Gin')
else : print('Lose')