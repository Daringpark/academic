
students = [15, 30, 50, 10]
students.sort() # [10, 15, 30, 50]
# without sort method? use min method
sum_time_cnt = 0
while len(students) != 1:
    time = students.pop(0)
    sum_time_cnt += time * len(students)
print(sum_time_cnt)
# 10 10 10
# 15 15
# 30

# This is min method
students = [15, 30, 50, 10]
sum_time_cnt = 0
while len(students) != 1:
    time = students.pop(students.index(min(students))) # index, pop(idx) time ++
    sum_time_cnt += time * len(students)
print(sum_time_cnt)

# It should be good to use sort and reverse if the data were too long.
students = [15, 30, 50, 10]
students.sort(reverse=1) # [10, 15, 30, 50]
# without sort method? use min method
sum_time_cnt = 0
while len(students) != 1:
    time = students.pop()
    sum_time_cnt += time * len(students)
print(sum_time_cnt)
