
# 끝난 시간을 기준으로 그리디하게 회의 시간을 가져가서 최대한 많이 회의를 진행하려고 한다.
schedule = [(1,4), (3,5), (1,6), (8,11), (5,7), (3,8), (6,10), (2,13), (5,9), (12,14)]
schedule.sort(key = lambda x: x[1])

idx = 0
start = schedule[idx][0]
end = schedule[idx][1]
cnt = 1

print(schedule[idx], cnt)
while idx < len(schedule): # idx가 끝까지 도달하였을 경우,
    while idx < len(schedule) and  end > schedule[idx][0]:
        idx += 1
    if idx < len(schedule):
        cnt += 1
        start = schedule[idx][0]
        end = schedule[idx][1]
        print(schedule[idx], cnt)