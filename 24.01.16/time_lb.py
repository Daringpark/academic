# 오늘 날짜 출력하기

# 나의 풀이
from datetime import date as dt
import datetime as td

deltatime_seoul = td.timedelta(hours = +9)
today = dt.today() + deltatime_seoul
# print(td.timedelta(hours = +9))
print(today)

# 다른 사람 풀이
import time
now = time
print(now.strftime('%Y-%m-%d'))