# 하루 출석으로 A 코인을 받을 수 있고, 월~일 7일 연속 출석시, 당일 A + B를 받는다.
# C 코인의 목표까지 도달하기 위해서는 최소 몇 일이 걸릴지 출력하시오.


total = cnt = 0
A, B, C = map(int, input().split())
while total < C:
    cnt += 1
    total += A
    if cnt%7 == 0:
        total += B
print(cnt)