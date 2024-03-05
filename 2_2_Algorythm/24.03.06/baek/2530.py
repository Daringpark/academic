
h, m, s = map(int, input().split())
second = int(input())
day = 0

hour_plus = second//3600
second %= 3600
minute_plus = second//60
second %= 60

day_plus = hour_plus//24
hour_plus %= 24
month_flag = 0

# print(hour_plus, minute_plus, second)
h += hour_plus
m += minute_plus
s += second
if s >= 60:
    s -= 60
    m += 1
if m >= 60:
    m -= 60
    h += 1
if h >= 24:
    h -= 24
    day += 1
if day >= 31:
    day -= 31
    month_flag += 1
    month_flag %= 4
# print(day)
print(h, m, s)